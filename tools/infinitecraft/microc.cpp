#include <ArduinoJson.h>
#include "WiFi.h" // Include the Wi-Fi library
#include <HTTPClient.h>
#include "time.h"

const char *ntpServer = "pool.ntp.org";
const long gmtOffset_sec = 3600;      // Adjust according to your timezone, in seconds
const int daylightOffset_sec = 3600;  // Daylight saving time offset
const char *ssid = "in Nonberg";      // Replace with your network SSID (name)
const char *password = "nuernberg88"; // Replace with your network password

// put function declarations here:
int myFunction(int, int);

class CookieManager
{
public:
  // Converts a JSON string of cookies into a single string for HTTP headers
  static std::string cookiesToString(const String jsonCookies)
  {
    // Parse JSON
    StaticJsonDocument<4096> doc;
    deserializeJson(doc, jsonCookies);

    std::string cookieHeader;
    for (JsonPair kv : doc.as<JsonObject>())
    {
      if (!cookieHeader.empty())
      {
        // Append "; " if not the first item
        cookieHeader += "; ";
      }
      cookieHeader += kv.key().c_str();
      cookieHeader += "=";
      cookieHeader += kv.value().as<std::string>();
    }
    return cookieHeader;
  }
};



void setup()
{

  HTTPClient http;

  // Correct usage with full URL for HTTP request
  // Ensure "https://" is included and use the correct path
  String payload = "";
  if (http.begin("http://192.168.178.20/cookies"))
  {
    int httpCode = http.GET();
    if (httpCode > 0)
    {
      Serial.printf("HTTP GET successful, code: %d\n", httpCode);
      if (httpCode == HTTP_CODE_OK)
      {
        payload = http.getString();
        //Serial.println(payload);
      }
    }
    else
    {
      Serial.printf("HTTP GET failed, error: %s\n", http.errorToString(httpCode).c_str());
    }
    http.end();
  }
  else
  {
    Serial.println("HTTP begin() failed");
  }

  // Convert JSON cookies to string
  std::string cookies = CookieManager::cookiesToString(payload);




  String serverName = "https://neal.fun/api/infinite-craft/pair";

   // Add your parameters directly to the server URL or use http.addParameter if supported
  String first_item = "Ocean";
  String second_item = "Ocean";
  String requestURL = serverName + "?first=" + first_item + "&second=" + second_item;
  
  http.begin(requestURL); // Start connection
  http.addHeader("Cookie", cookies.c_str());
  // Add other headers as necessary
  http.addHeader("Authority", "neal.fun");
  http.addHeader("Accept", "*/*");
  http.addHeader("Accept-Encoding", "gzip, deflate, br, zstd");
  http.addHeader("Accept-Language", "en-US,en;q=0.9");
  http.addHeader("Referer", "https://neal.fun/infinite-craft/");
  http.addHeader("Sec-Fetch-Dest", "empty");
  http.addHeader("Sec-Fetch-Mode", "cors");
  http.addHeader("Sec-Fetch-Site", "same-origin");
  http.addHeader("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36");
  
 
 
 

  int httpCode = http.GET();
  if (httpCode > 0)
  {
    String payload = http.getString();
    Serial.println(payload);
  }
  else
  {
    Serial.println("Error on HTTP request");
  }

  http.end();
}

void loop()
{
  // put your main code here, to run repeatedly:
}

// put function definitions here:
int myFunction(int x, int y)
{
  return x + y;
}