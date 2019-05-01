main:
	@for i in 0 1; \
	do \
		echo "------------------------------------------------------------------------"; \
		echo Testing sample $$i; \
		python3 main.py < input-$$i.txt > output-$$i.txt && \
		diff -y output-$$i.txt output-sample-$$i.txt; \
		echo "------------------------------------------------------------------------"; \
	done
