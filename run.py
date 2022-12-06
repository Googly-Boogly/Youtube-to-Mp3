from script import run_script

def run():
    movie = input('Enter Movie Name: ')
    links = []
    while True:

        temp = input('If done write "done": else enter link: ')
        if temp == 'done':
            # print('break')
            break
            # print('break2')
        else: 
            links.append(temp)
    for x in links:
        run_script(movie, x)
        # print('hey')

run()