install:
		poetry install

brain-games:
		poetry run brain-games

build:
		poetry build

publish:
		poetry publish --build --dry-run

package-install:
		pipx install --force dist/*.whl

lint:
		poetry run flake8
