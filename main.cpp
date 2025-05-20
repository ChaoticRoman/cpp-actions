#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

0

int main(int argc, char **argv)
{
    std::ifstream f("example.json");

    json data = json::parse(f);

    std::cout << data.dump() << std::endl;

    return 0;
}
