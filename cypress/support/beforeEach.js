beforeEach(function () {
  // Reset DB before each test
  // TODO: find a faster way to do this.
  cy.exec(
    "docker-compose run web sh -c './manage.py flush --noinput && ./manage.py generate_test_data'"
  );

  /**
   * This command performs the same function as the docker-based command above,
   * except when running tests in a local, non-containerized environment.
   *
   * It specifies a test database that should be created beforehand
   */
  // cy.exec(
  //   `source .venv/bin/activate && DATABASE_URL="postgres:///modernomad/test" python manage.py flush --no-input && DATABASE_URL="postgres:///modernomad/test" python manage.py generate_test_data`
  // );
});
