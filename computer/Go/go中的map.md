# Go-N?vmap



> (Wgo-N?N*Nmap/fN*N?T^h??v_(u0?T^h?/fN*N.?<P?[?vƖT0



## R?^N*Nmap



?Qn?vmake?QpeR?^map



```go

m := make(map[string]int) // ?Nstring0Rint?v f\

m["who"] = 100

```



O(ugoW[b?ϑR?^map?T?e؝?S?Nc?[N?NgR?vkey/value



```go

m := map[string]int{

    "alice": 10,

    "charlie": 34

}

```



## map?vN?N?d\O



### M??Smap



```go

for name, age := range ages {

    fmt.Println("%s\t%d\n", name, age)

}

```



## $R?e.?/f&TX[(W



```go

value, ok := ages["who"]

if !ok {

    /* */

}

```



## O(udelete()?Qpe Rd?.?<P?[



```go

delete(m, "clz")

```



## 	cgqc?[z??^M??Smap



HQO(usort!jWW?[.??c?^?6qT	c.?z??^?S<P0



```go

import "sort"



var names []string

for name := range ages {

    names = append(names, name)

}

sort.Strings(names)

for _, name := range names {

    fmt.Printf("%s\t%d\n", name, ages[name])

}

```



## \map(u\Oset



go틊-Nv^?l	gset{|?W?FO/fmap-N?vkey/f
N?S͑
Y?@b?N?S?N\map(u\Oset



```go

seen := make(map[string]bool) // a set of strings

```



?S?N\ٝ?y?_euvalue?vmapS_\ON*NW[&{2NƖT0



ٝ̑b?`0R?Njava?vHashSet?1\/f?W?N?T^h??vset



## map?v?St



![1aa15e9f3d78b3e66dacbead2990f78aa08.jpg](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c2c888d76594f13a63ebb959e7ddb59~tplv-k3u1fbpfcp-watermark.image)



teSO
Nw?go?vmapǑ(ud?YuYOpe?leg۝L??T^Н?{0Ǒ(u?b???legYt?T^?Q?z?sSO(u??h?egX[?P?T^?~?g?vT?vCQ }0`??
NNjava?vHashMap?vT??S/fwQSO?[?s
N
N'Y?vT0



sQ?Ngo-Nmap?vwQSO?[?s?\(WN?{?e?z-NwQSO???0



## ?S?D??e



1. http://www.topgoer.com/ 
0Go틊-N?e?ech0

2. https://docs.hacknode.org 
0Go틊#W?~0

3. https://blog.csdn.net/qq_38572383/article/details/95359805

