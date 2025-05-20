pretty-json: main.cpp
	g++ main.cpp -o $@

test:
	pytest tests

clean:
	rm pretty-json
