
acertos = 0;
n = 100000;
i=0;
for i = 0:n
    x=2*rand(1,1)-1;
    y=2*rand(1,1)-1;
    if x.^2 + y.^2 < 1
        acertos = acertos + 1
    end
    i=i+1;
end
pi = acertos*4./n