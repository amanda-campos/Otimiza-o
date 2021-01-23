% Exercício 4: Simulated Annealing
X0 = 0; 
J0 = -X0+100*(X0-0.2)^2*(X0-0.8)^2;  
Xatual = X0; 
Jatual = J0;

%Definições
N = 10; 
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
    n = n + 1; 
    
    X = Xatual + e*rand(size(Xatual));
    
    J = -X+100*(X-0.2)^2*(X-0.8)^2; 
   
    if  rand(1)<exp((Jatual-J)/T);
        
        Xatual = X 
        Jatual = J ;
    end;
    if J<Jmin,
        Jmin = J;
        Xmin = X
    end;
    if (rem(n,N)==0),
        k = k+1;
        T = T0/log2(1+k);
        if k==K, 
            fim = 1; 
        end;
    end;
end;
