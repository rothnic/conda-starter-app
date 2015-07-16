
build:
	docker build -t example_conda_app .

run: build
	docker run --rm example_conda_app
