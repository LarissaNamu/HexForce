#include <curl/curl.h>
#include <nlohmann/json.hpp>
#include <iostream>
#include <fstream> // For file handling
#include <string>

int main(){
    nlohmann::json testJson = {{"key", "value"}};
    return 0;
}