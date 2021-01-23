% Exercício 3: Simulated Annealing
X0 = 0.1; 
J0 = (X0)^2;  
Xatual = X0 ;
Jatual = J0;

%Definições
N = 10;
T = 0.1;
e = 0.1; 
fim = 0;
n = 0;

while not(fim),
    n = n + 1; 
    
    X = Xatual + e*randn(size(X));
    
    dJ = (X)^2 - (Xatual)^2;
    
    q = exp(-dJ/T);
   
    r = rand(1);
    
    if r > q
        a=0;
    end
    if r < q
        a = 1;
    end
    if dJ < 0
        Xatual = X
    end
    if dJ >= 0
        Xatual = (1-a)*Xatual + a*X
    end
    
    if n == N
        fim = 1;
    end
end
