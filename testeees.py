import speedtest

test = speedtest.Speedtest()
down = test.download()
upload = test.upload()

print(f'donwload speed: {down}')
print(f'upload speed: {upload}')