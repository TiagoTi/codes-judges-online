CASES_TO_TESTS = 0 1 2


main: inputs outputs
	@for i in ${CASES_TO_TESTS}; \
	do \
		echo "------------------------------------------------------------------------"; \
		echo Testing sample $$i; \
		python3 main.py < input-$$i.txt > output-$$i.txt && \
		diff -y output-$$i.txt output-sample-$$i.txt; \
		echo "------------------------------------------------------------------------"; \
	done


inputs:
	@for i in ${CASES_TO_TESTS}; \
	do \
		touch input-$$i.txt; \
	done


outputs:
	@for i in ${CASES_TO_TESTS}; \
	do \
		touch output-sample-$$i.txt; \
	done


sonar:
	../../../bin/sonar-python.sh
