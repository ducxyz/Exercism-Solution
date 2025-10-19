def prime(n): # n = 2
    if n == 0 : 
        raise ValueError('there is no zeroth prime')
    if n == 1 :
        return 2
    primes = [2]
    candidate = 3

    while len(primes) < n :
        is_prime = True

        for p in primes :
            if p * p > candidate :
                break
            if candidate % p == 0 :
                is_prime = False
                break
        if is_prime == True : 
            primes.append(candidate)

        candidate += 2

    return primes[n-1]




        
            

    
    
    
    

