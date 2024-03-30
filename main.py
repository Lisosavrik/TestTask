from testtask.main.tasks import testing

result = testing.delay()
print(result.get())

