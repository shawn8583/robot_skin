function y=lagrange(x0,y0,x) 
%拉格朗日插值函数 
%n 个节点数据以数组 x0, y0 输入(注意 Matlat 的数组下标从1开始), 
%m 个插值点以数组 x 输入,输出数组 y 为 m 个插值 
n=length(x0);m=length(x); 
for i=1:m 
z=x(i); 
s=0.0; 
for k=1:n 
      p=1.0; 
      for j=1:n 
           if j~=k 
              p=p*(z-x0(j))/(x0(k)-x0(j)); 
           end 
      end 
      s=p*y0(k)+s; 
end 
y(i)=s; 
end