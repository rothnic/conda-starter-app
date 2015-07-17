FROM example_conda_app

RUN fab install_test

COPY . /app/tests
COPY .pylintrc /app/.pylintrc
CMD ["/app/tests/test.sh"]
