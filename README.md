# Example project to showcase GitHub actions for C++ projects

## The code to work on

I would like it to have at least one dependency and tests to make actions not so trivial.

Let's go with json pretty printer for example, let us use [Niels Lohmann's json library][json]
for that. **TODO**

[json]: https://github.com/nlohmann/json

## Dependencies

Install dependencies on Ubuntu 24.04.2 LTS:

```
sudo apt install make g++ nlohmann-json3-dev
```

## Build

```
make
```

## Run

```
./pretty-json
```

## Actions

Let us have following actions:

* It builds.
* It conforms to style **TODO**
* Linter is happy **TODO**
* Let us add AI generated code review **TODO**

## Resources

* https://docs.github.com/en/actions
* https://docs.github.com/en/actions/use-cases-and-examples/creating-an-example-workflow
* https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions
