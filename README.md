# pairing
 studio di funzioni di pairing NxN->N
 
 ## triangle pairing
 ![triangle pairing picture](https://github.com/lucadonnoh/pairing/blob/master/trianglepairing.png?raw=true)
 
 Genera i numeri utilizzando la funzione f^-1: N->NxN.
 
 ### derivazione della funzione f: NxN->N
 Si nota che i punti su una stessa diagonale hanno una cosa in comune: hanno lo stesso x+y=n.
 
 Si cerca una funzione NxN->N che vale per le coppie <x,0>.
 
 Provando a caso, ho notato che una funzione possibile è g(x) = x(x+1)/2, che è equivalente a n(n+1)/2;
 
 Si nota che g è la funzione generatrice dei numeri triangolari (di gauss?).
 
 In effetti g ha senso in quanto prima dell'n-esimo numero che si trova sull'asse delle x ci sono (n-1)+(n-2)+...+1 numeri.
 
 I numeri successivi nella stessa diagonale sono il numero b alla base della diagonale + il loro y.
 
 La funzione è quindi: f(<x,y>): (x+y)(x+y+1)+y.
 
 La funzione inversa è troppo difficile da trovare, ma siccome f è biettiva allora esiste (not sure? ma intuitivamente sembra così).
 
 
 

## square pairing
![square pairing picture](https://github.com/lucadonnoh/pairing/blob/master/squarepairing.png?raw=true)

## pentagon pairing ??

## polygon pairing ??
