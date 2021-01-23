% Exercício 5: Simulated Annealing
X0 = 0; 
J0 = (X0-2)^4/4-2*(X0-2)^3/3-(X0-2)^2/2+2*(X0-2)-2;  
Xatual = X0; 
Jatual = J0;

%Definições
N = 100; 
K = 8;
T0 = 5e-3;
e = 5e-2; 
fim = 0;
n = 0;
k = 1;
Jmin = Jatual;
Xmin = Xatual;
T = 0.1; 

while not(fim),
    n = n + 1 
    
    X = Xatual + e*randn(size(Xatual))
    
    J = (X-2)^4/4-2*(X-2)^3/3-(X-2)^2/2+2*(X-2)-2 
   
    if  rand(1)<exp((Jatual-J)/T)
        
        Xatual = X 
        Jatual = J 
    end;
    if J<Jmin,
        Jmin = J
        Xmin = X
    end;
    if (rem(n,N)==0),
        k = k+1
        T = T0/log2(1+k)
        if k==K, 
            fim = 1; 
        end;
    end;
end;
