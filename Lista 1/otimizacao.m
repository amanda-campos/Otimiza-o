% 070403 gabriel@pads.ufrj.br

clear all;
randn('state',0); rand('state',0); P=5;
X = randn(2,P);
X0 = zeros(2,1);
JA = mean(sum((X - repmat(X0,1,P)).^2,1));
lambda = 0.5;
JB = 0;
for i=1:P,
    for j=(i+1):P,
        JB = JB + 1/sum((X(:,i)-X(:,j)).^2);
    end;
end;
JB = JB/(P*(P-1)/2);
J0 = JA + lambda*JB; % Custo Inicial

epsilon = 1e-1; T0 = 0.5; M = 1000000;
fim = 0;
J = J0; 
k = 1;

Jc = J; Xc = X; BK_J = zeros(M,1); Jmin = J;
while not(fim),    
    T = T0 / log2(1+k); % T = T0, Temperatura Fixa
    for n=1:M,        
        X = Xc + epsilon*randn(size(X)); % Note variacao continua de X
        JA = mean(sum((X - repmat(X0,1,P)).^2,1)); JB = 0; for i=1:P, for j=(i+1):P, JB = JB + 1/sum((X(:,i)-X(:,j)).^2); end; end; JB = JB/(P*(P-1)/2); J = JA + lambda*JB;
        if rand(1,1)<exp((Jc-J)/T),
            Xc = X; Jc = J;
        end;
        if J < Jmin,
            Jmin = J;
            Xmin = X;
        end;
        BK_J(n) = Jc;
        if (rem(n,floor(M/100))==0),
            percent_complete = floor(n/M*100)
        end;
    end;
    % k = k+1; - Temperatura Fixa
    fim=1;
end;

L=M/10; A=1; B=L; EJ = mean(BK_J(A:B));
for k=2:10, A=A+L; B=B+L; EJ(k) = mean(BK_J(A:B)); end;
figure; [H,C] = hist(BK_J((M-L+1):M),50); stem(C,H/L); grid on; axis([1 10 0 0.35]);
xlabel('Jbar'); ylabel('Azul: P(Jbar) (Jbar v.a. discreta). Vermelho: exp(-Jbar/T)'); title('T = 0.5');
p = exp(-C/T); p = p/sum(p); hold on; plot(C,p,'r.');

% Alguns Resultados Obtidos com T = 0.5:

% >> X'
% 
% ans =
% 
%    1.61654398093754  -1.99564445974705
%    1.61890156209262   0.89142960583890
%   -0.62496376224270  -0.44961075150673
%    1.08259382110564   0.02024242182650
%   -0.73098841566943   0.07515863119041
% 
% >> Xmin'
% 
% ans =
% 
%   -0.56041475299671   0.83944413935334
%   -0.46952610490406  -0.66876053984408
%    0.67122091947419  -0.50395147079294
%    0.55565691768270   0.58316621085484
%   -0.24775688951660   0.01085824954518
% 
% >> Jmin
% 
% Jmin =
% 
%    1.05194281105370
% 
% >> EJ'
% 
% ans =
% 
%    3.00693313216586
%    2.93880096886439
%    3.12767744606877
%    3.15058609303355
%    3.03001502290623
%    3.14878689814057
%    3.02199219231481
%    3.13159981196455
%    3.09841529093937
%    3.15027968312081