#Usage: make push m="Push message"

push:
	git pull
	git add .
	git commit -m "$m"
	git push