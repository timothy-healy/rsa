# diffie-hellman
This repository is for a short demonstration of Diffie-Hellman key exchange; a preliminary version using built-in Python libraries before
creating my own implementations.

The Diffie-Hellman key exchange is a method of exchanging a shared secret value over an insecure communication channel.
Both parties agree upon a large prime $p$ to be used as a modulus and a nonzero integer $g$.
Ideally, the order of $g$ in the finite field with $p$ elements is a large prime.
Both $p$ and $g$ are considered public information since they are shared over the insecure channel.
Each party chooses another integer that they do not share.
Both parties now calculate the value $g$ raised to the power of their secret integer mod $p$.
They exchange these computed values over the communication channel.
Lastly, each party raises this newly received value to the power of their secret integer mod $p$.
They will have calculated the same value, and now each know a secret value that was never exchanged over the channel.

This method is secure because anyone that only has the public information must solve the Discrete Logarithm Problem, in order to calculate the secret value that was exchanged.
Thus, in practice, the chosen numbers $p$ and $g$ would be much larger than shown in this demonstration, on the order of $2^{1000}$.
Otherwise, the Discrete Logarithm Problem can be easily solved by brute force, trying every single possible value.

## Usage
```
python dh.py
Agreed upon large prime p: 148045384080202133955635193775791823697006751534544273715940344330190098923
Agreed upon integer base g: 41425139533777157882218459049007860621663054162185016681138642194863405503
Resulting exchange:
Alice's public key sent to Bob: 96244035467393348871201106747605627703685422334677233590776468732777852202
Bob's public key sent to Alice: 134714807855222076430383313599686960136602304140947447753778520211965254349
Alice calculates secret value as: 133893366189321145616888408279017724738035149338796018873170956866806264779
Bob calculates secret value as: 133893366189321145616888408279017724738035149338796018873170956866806264779
Calculated the same value: True
```
