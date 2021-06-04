from time import time
from multiprocessing import Process

def factorize (*value):
    
    
    for val in value:
        result = []
        for i in range(1, val + 1):
            if val%i == 0:
                result.append(i)
        
        print(result)



if __name__ == "__main__":

    start_time = time()
    factorize(128, 255, 99999, 10651060)
    end_time = time()
    
    print(end_time - start_time)


    start_time_1 = time()
    process_1 = Process(target=factorize, args=(128, ))
    process_2 = Process(target=factorize, args=(255, ))
    process_3 = Process(target=factorize, args=(99999, ))
    process_4 = Process(target=factorize, args=(10651060, ))

    process_1.start()
    process_2.start()
    process_3.start()
    process_4.start()

    process_1.join()
    process_2.join()
    process_3.join()
    process_4.join()

    end_time_1 = time()
    print(end_time_1 - start_time_1)