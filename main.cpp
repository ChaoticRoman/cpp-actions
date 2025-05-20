#include <filesystem>
#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

int main(int argc, char **argv) {
  std::ifstream f(argv[1]);

  json data = json::parse(f);

  std::cout << data.dump() << std::endl;

  return 0;
}
