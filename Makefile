help:
	@echo make run
	@echo make test
	@echo make stats

run:
	python3 device.py

test:
	python3 test_device.py

stats:
	python3 stats.py
