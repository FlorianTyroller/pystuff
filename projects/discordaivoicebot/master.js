const { Client, GatewayIntentBits } = require('discord.js');
const { joinVoiceChannel, createAudioPlayer, createAudioResource, AudioPlayerStatus, getVoiceConnection } = require('@discordjs/voice');
const prism = require('prism-media');
const fs = require('fs');
const path = require('path');
const ffmpeg = require('ffmpeg-static');
const { exec } = require('child_process');
const { opus } = require('prism-media');
const { Transform } = require('stream');
const { createClient } = require("@deepgram/sdk");
const axios = require('axios');
require('dotenv').config();


let isRecording = false;
const token = process.env.DISCORD_BOT_TOKEN; // Replace this with your bot's token




const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildVoiceStates,
        GatewayIntentBits.MessageContent,
        GatewayIntentBits.GuildMessages,
    ]
});




client.once('ready', () => {
    console.log('Ready!');
});



client.on('messageCreate', async message => {
    if (!message.guild) return;

    if (message.content.startsWith('!speaktts') && false) {
        // Extract the text after "!speaktts" and trim any extra whitespace
        const text = message.content.slice('!speaktts'.length).trim();

        // Check if the extracted text is empty and handle accordingly
        if (text.length === 0) {
            message.channel.send("Please provide some text after '!speaktts'.");
            return;
        }

        // Now call your function with the cleaned text
        speakText(message, text);
    }

    if (message.content === '!join') {
        if (message.member.voice.channel) {
            const connection = joinVoiceChannel({
                channelId: message.member.voice.channel.id,
                guildId: message.guild.id,
                adapterCreator: message.guild.voiceAdapterCreator,
                selfDeaf: false, // Ensure the bot is not deafened
            });

            message.reply('Joined your voice channel!');
        } else {
            message.reply('You need to join a voice channel first!');
        }
    } else if (message.content === '!recorder' && !isRecording) {
        startRecording(message);
    } else if (message.content === '!stoprecorder' && isRecording) {
        stopRecording();
        //message.reply('Recording has been stopped.');
    }
});


const startRecording = async(message) => {
    if (!message.member.voice.channel) {
        message.reply('Please join a voice channel first!');
        return;
    }

    isRecording = true;
    const voiceChannel = message.member.voice.channel;
    const connection = joinVoiceChannel({
        channelId: voiceChannel.id,
        guildId: voiceChannel.guild.id,
        adapterCreator: voiceChannel.guild.voiceAdapterCreator,
        selfDeaf: false
    });
    // 214104585307029505 // kammerer
    //message.member.id
    const audioStream = connection.receiver.subscribe("256810338685681665", { mode: 'pcm' });
    const outputStream = new prism.opus.Decoder({ rate: 48000, channels: 2, frameSize: 960 });
    const pcmFile = path.join(__dirname, 'output.pcm');
    const mp3File = path.join(__dirname, 'output.mp3');

    // Delete existing files if they exist
    [pcmFile, mp3File].forEach(file => {
        if (fs.existsSync(file)) {
            fs.unlinkSync(file);
        }
    });

    const writeStream = fs.createWriteStream(pcmFile);

    function cleanup() {
        //audioStream.destroy(); // Properly stop receiving audio data
        outputStream.end(); // Close the output stream
        writeStream.end(); // Make sure to close the write stream

        // Remove any listeners that were added to avoid memory leaks
        audioStream.removeAllListeners();
        outputStream.removeAllListeners();
        writeStream.removeAllListeners();
    }



    const silenceDetector = createSilenceDetectorStream(100, 1500, writeStream, () => {
        convertPcmToMp3(pcmFile, mp3File, (error) => {
                if (error) {
                    message.channel.send('Error converting audio to MP3.');
                    return;
                }
                //message.channel.send('Recording stopped and saved to file as MP3.');

                // Now call the transcribe function
                transcribeFile(message, (msg, error, result) => {
                    if (error) {
                        msg.channel.send('Error during transcription: ' + error.message);
                        console.error('Transcription error:', error);
                        return;
                    }
                    handleTranscriptionResult(msg, result);
                    if (isRecording) {
                        //console.log("before cleanup")
                        cleanup();
                        //console.log("after cleanup")
                        setTimeout(() => {
                            console.log("restarted");
                            startRecording(message); // Restart recording after a delay
                        }, 300);
                    }
                });
            },
            () => {
                console.log("MP3 conversion completed successfully.");

                // Call transcribeFile or any other function as required.
            });
    });



    audioStream.pipe(outputStream).pipe(silenceDetector).pipe(writeStream);

};

const stopRecording = () => {
    isRecording = false;
    // Additional cleanup logic if necessary
};
const speakText = async(message, text) => {
    try {


        await convertTextToSpeech(text, message); // Wait until the audio file is completely written
        const filePath = "outpute.mp3";

        let connection = getVoiceConnection(message.guild.id);
        if (!connection && message.member.voice.channel) {
            connection = joinVoiceChannel({
                channelId: message.member.voice.channel.id,
                guildId: message.guild.id,
                adapterCreator: message.guild.voiceAdapterCreator,
            });
        }

        if (connection) {
            const player = createAudioPlayer();
            const resource = createAudioResource(filePath);
            player.play(resource);
            connection.subscribe(player);

            player.on(AudioPlayerStatus.Playing, () => {
                console.log('Playing audio file!');
            });

            player.on(AudioPlayerStatus.Idle, () => {
                player.stop(); // Stop the player when finished
                console.log('Finished playing!');
            });

            player.on('error', error => console.error(`Error: ${error.message}`));
        } else {
            message.reply("You need to be in a voice channel.");
        }

    } catch (error) {
        console.error('Failed to process transcription result:', error);
        message.channel.send('Failed to process the transcription result.');
    }
};



const handleTranscriptionResult = async(message, result) => {
    try {
        if (!result || !result.result || !result.result.results || !result.result.results.channels || result.result.results.channels.length === 0) {
            throw new Error("Invalid or empty transcription result.");
        }
        let transcript = result.result.results.channels[0].alternatives[0].transcript;

        if (transcript.length > 3) {
            message.channel.send(`Transcript: "${transcript}"`);
            await convertTextToSpeech(transcript, message); // Wait until the audio file is completely written
            const filePath = "outpute.mp3";

            let connection = getVoiceConnection(message.guild.id);
            if (!connection && message.member.voice.channel) {
                connection = joinVoiceChannel({
                    channelId: message.member.voice.channel.id,
                    guildId: message.guild.id,
                    adapterCreator: message.guild.voiceAdapterCreator,
                });
            }

            if (connection) {
                const player = createAudioPlayer();
                const resource = createAudioResource(filePath);
                player.play(resource);
                connection.subscribe(player);

                player.on(AudioPlayerStatus.Playing, () => {
                    console.log('Playing audio file!');
                });

                player.on(AudioPlayerStatus.Idle, () => {
                    player.stop(); // Stop the player when finished
                    console.log('Finished playing!');
                });

                player.on('error', error => console.error(`Error: ${error.message}`));
            } else {
                message.reply("You need to be in a voice channel.");
            }
        }
    } catch (error) {
        console.error('Failed to process transcription result:', error);
        message.channel.send('Failed to process the transcription result.');
    }
};

async function convertTextToSpeech(text, message) {
    const options = {
        method: 'POST',
        headers: {
            'xi-api-key': process.env.ELEVENLABS_KEY,
            'Content-Type': 'application/json'
        },
        data: {
            text: text,
            model_id: "eleven_multilingual_v2",
            voice_settings: {
                stability: 0.5,
                similarity_boost: 0.5
            }
        },
        url: 'https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB?output_format=mp3_22050_32&optimize_streaming_latency=4',
        responseType: 'stream'
    };

    // Return the axios promise
    return axios(options)
        .then(response => {
            const writer = fs.createWriteStream('outpute.mp3');
            response.data.pipe(writer);

            // Return a new promise that resolves when the file has been fully written
            return new Promise((resolve, reject) => {
                writer.on('finish', () => {
                    console.log('File has been written successfully.');
                    resolve(); // Resolve the promise when the file writing is done
                });
                writer.on('error', reject);
            });
        })
        .catch(err => {
            console.error('Error writing file:', err);
            throw err; // Ensure to throw the error to be caught by the caller
        });
}

function convertPcmToMp3(inputFile, outputFile, callback, onConversionComplete) {
    const command = `${ffmpeg} -f s16le -ar 48000 -ac 2 -i ${inputFile} ${outputFile}`;
    exec(command, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${error.message}`);
            console.log('Audio not converted to MP3 format successfully!');
            callback();
            return;
        }
        if (stderr) {
            //console.error(`stderr: ${stderr}`);
            console.log('Audio converted to MP3 format successfully!');
            callback();
            onConversionComplete();
            return;
        }
        console.log('Audio converted to MP3 format successfully!');
        callback();
    });
}

const transcribeFile = async(message, callback) => {
    const deepgramApiKey = process.env.DEEPGRAM_KEY;
    const pathToFile = "output.mp3";
    const deepgram = createClient(deepgramApiKey);

    try {
        const result = await deepgram.listen.prerecorded.transcribeFile(
            fs.createReadStream(pathToFile), { punctuate: true, model: 'nova-2', language: 'de' }
        );
        //console.log("Transcription result:", JSON.stringify(result, null, 2)); // Log the full result
        callback(message, null, result); // Pass message and result back
    } catch (error) {
        console.error('Transcription error:', error);
        callback(message, error);
    }
};

function createSilenceDetectorStream(threshold, silenceTimeout, writeStream, onFinish) {
    let lastSoundTime = Date.now();
    let timeoutHandler;
    let recording = false;
    let done = false

    const updateLastSoundTime = () => {
        if (!recording) {
            recording = true;
            console.log("Voice detected, starting recording...");
            // Attach the finish event listener as soon as we start recording
            writeStream.on('finish', () => {

                onFinish(); // Ensure onFinish is called only after the writeStream is fully closed

            });
        }
        lastSoundTime = Date.now();
        if (!timeoutHandler) { // Start the timeout handler if it has not been started
            timeoutHandler = setTimeout(checkSilence, silenceTimeout);
        }
    };

    const checkSilence = () => {
        const timeSinceLastSound = Date.now() - lastSoundTime;
        if (recording && timeSinceLastSound >= silenceTimeout) {
            console.log("Silence detected, stopping recording...");
            done = true;
            recording = false;
            clearTimeout(timeoutHandler);
            writeStream.end();
            timeoutHandler = null;
        } else {
            // Reset the timeout to check again after the remaining time
            clearTimeout(timeoutHandler);
            timeoutHandler = setTimeout(checkSilence, silenceTimeout - timeSinceLastSound);
        }
    };

    return new Transform({
        transform(chunk, encoding, callback) {
            const amplitude = calculateAmplitude(chunk);
            if (amplitude > threshold && !done) {
                updateLastSoundTime();
            }
            if (recording) {
                this.push(chunk);
            }
            callback();
        },
        final(callback) {
            clearTimeout(timeoutHandler);
            callback();
        }
    });
}


function calculateAmplitude(buffer) {
    let rms = 0;
    let count = 0;
    for (let i = 0; i < buffer.length - 1; i += 2) {
        if (i + 1 >= buffer.length) {
            break; // Break the loop if there aren't enough bytes left for a full int16
        }
        const int16 = buffer.readInt16LE(i);
        rms += int16 * int16;
        count++;
    }
    rms = count > 0 ? Math.sqrt(rms / count) : 0;
    return rms;
}

client.login(token);