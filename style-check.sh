find . -iname '*.hpp' -o -iname '*.cpp' -o  -iname '*.h' | xargs clang-format --dry-run --Werror
