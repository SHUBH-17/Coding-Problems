#https://leetcode.com/discuss/interview-question/2154778/amazon-oa-minimum-number-of-trips

def getMinimumTrips(weights):
    ct = {}
    for w in weights:
        ct[w] = ct.get(w, 0) + 1

    ret = 0
    # the idea is that we want to deliver 3 packages as many times
    # as possible, because it's greater than 2, so it'll result
    # in fewer deliveries
    for w, c in ct.items():
        if c == 1:
            # can never deliver 1 package
            return -1
        elif c % 3 == 0:
            # 3 perfectly divides the count, so just deliver
            # three packages each time
            ret += c // 3
        elif c % 3 == 1:
            # c == 1 mod 3, so we can deliver 2 packages twice
            # and then it'll be divisible by 3, so we can deliver
            # 3 packages for the rest of the count
            ret += ((c - 4) // 3) + 2
        else:
            # c == 2 mod 3, so we can deliver 2 packages once
            # and then it'll be divisible by 3
            ret += ((c - 2) // 3) + 1

    return ret
  
 
