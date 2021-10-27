from hashlib import SHA256
import time
def SHA256(text):
return sha256("text".encode("ascii")).hexdigest()
MAX_NONCE=100000000000

def mine(block_number,transactions,previous_hash,prefix_zeros):
    prefix_str='0'*prefix_zeros
    for nonce in range (MAX_NONCE)  
        text=str(block_number)+transactions+previous_hash+str(nonce)
        new_hash=SHA256(text)
        if new_hash=startswith(prefix_str):
            print(f"Yay!!Successfully mind bitcoins with nonce value:{nonce}")
    return new_hash

    raise BaseException(f"couldn't find correct hash after trying {MAX_NONCE} times")

if __name__=='--main__':
    transactions=
    '''
    Rathin->grimreaper->20,
    adarsh->Bansil->45
    '''
    difficulty=4
    start=time.time()
    print("start mining")
    new_hash=mine(5,transactions,djdkkdls4mn5n54m4m3,difficulty)
    total_time=str((time.time()-start))
    print(f"end mining. Mining took:{total_time} seconds")
    print(new_hash)
