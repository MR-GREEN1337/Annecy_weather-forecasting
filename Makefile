#Usage: make push m="Push message"

# Usage: make push

push:
	git pull
	git add .
	@read -p "Enter your commit message: " message; \
	git commit -m "$$message"
	git push
