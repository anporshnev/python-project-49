install:
		poetry install

brain-games:
		poetry run brain-games

brain-calc:
		poetry run brain-calc

brain-even:
		poetry run brain-even

brain-gcd:
		poetry run brain-gcd

brain-prime:
		poetry run brain-prime

brain-progression:
		poetry run brain-progression

build:
		poetry build

publish:
		poetry publish --build --dry-run

package-install:
		pipx install --force dist/*.whl

lint:
		poetry run flake8
