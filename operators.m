BViolatingOperatorsDim8 = <|

  "9" -> Op[Wt[G["9"][p, q, r, s]],
            L[p, i], Q[q, j], Conj[ub[r]], Conj[ub[s]], Conj[H[k]], Conj[H[l]],
            Eps[i, k], Eps[j, l]
         ],

  "10" -> Op[Wt[G["10"][p, q, r, s]],
             Conj[eb[p]], Q[q, i], Q[r, j], Conj[db[s]], H[k], H[l],
             Eps[k, i], Eps[j, l]
          ],

  "11" -> Op[Wt[G["11"][p, q, r, s]],
             L[p, i], Q[q, j], Conj[db[r]], Conj[db[s]], H[k], H[l],
             Eps[k, i], Eps[j, l]
          ],

  "12a" -> Op[Wt[G["12a"][p, q, r, s]],
              L[p, i], Q[q, j], Q[r, k], Q[s, l], H[m], Conj[H[n]],
              Eps[i, l], Eps[j, m], Eps[k, n]
           ],

  "12b" -> Op[Wt[G["12b"][p, q, r, s]],
              L[p, i], Q[q, j], Q[r, k], Q[s, l], H[m], Conj[H[n]],
              Eps[i, m], Eps[j, l], Eps[k, n]
           ],

  "12c" -> Op[Wt[G["12c"][p, q, r, s]],
              L[p, i], Q[q, j], Q[r, k], Q[s, l], H[m], Conj[H[n]],
              Eps[i, k], Eps[j, l], Eps[m, n]
           ],

  "12d" -> Op[Wt[G["12d"][p, q, r, s]],
              L[p, i], Q[q, j], Q[r, k], Q[s, l], H[m], Conj[H[n]],
              Eps[i, n], Eps[j, l], Eps[k, m]
           ],

  "13a" -> Op[Wt[G["13a"][p, q, r, s]],
              Conj[eb[p]], Q[q, i], Q[r, j], Conj[ub[s]], H[k], Conj[H[l]],
              Eps[i, k], Eps[j, l]
           ],

  "13b" -> Op[Wt[G["13b"][p, q, r, s]],
              Conj[eb[p]], Q[q, i], Q[r, j], Conj[ub[s]], H[k], Conj[H[l]],
              Eps[i, j], Eps[k, l]
           ],

  "14" -> Op[Wt[G["14"][p, q, r, s]],
             Conj[eb[p]], Conj[ub[q]], Conj[ub[r]], Conj[db[s]], H[i], Conj[H[j]],
             Eps[i, j]
          ],

  "15a" -> Op[Wt[G["15a"][p, q, r, s]],
              L[p, i], Q[q, j], Conj[ub[r]], Conj[db[s]], H[k], Conj[H[l]],
              Eps[i, k], Eps[j, l]
           ],

  "15b" -> Op[Wt[G["15b"][p, q, r, s]],
              L[p, i], Q[q, j], Conj[ub[r]], Conj[db[s]], H[k], Conj[H[l]],
              Eps[i, l], Eps[j, k]
           ],

  "15c" -> Op[Wt[G["15c"][p, q, r, s]],
              L[p, i], Q[q, j], Conj[ub[r]], Conj[db[s]], H[k], Conj[H[l]],
              Eps[i, j], Eps[k, l]
           ]

|>;

BViolatingOperatorsDim9 = <|

  "19"  -> Op[Wt[G["19"][p,q,r,s,t,u]],
              Conj[eb[p]], Conj[eb[q]], eb[r], db[s], db[t], db[u]
           ],

  "20"  -> Op[Wt[G["20"][p,q,r,s]],
              Conj[eb[p]], Conj[Q[q,i]], Conj[Q[r,j]], Conj[Q[s,k]], H[l], H[m], H[n],
              Eps[i, l], Eps[j, m], Eps[k, n]
           ],

  "21"  -> Op[Wt[G["21"][r,s,t,u,v,w]],
              Conj[eb[r]], db[s], db[t], db[u], db[v], Conj[db[w]]
           ],

  "22"  -> Op[Wt[G["22"][r,s,t,u,v,w]],
              L[r,i], L[s,j], eb[t], ub[u], db[v], db[w],
              Eps[i,j]
           ],

  "23"  -> Op[Wt[G["23"][r,s,t,u,v,w]],
              Conj[eb[r]], Conj[Q[s,i]], Conj[Q[t,j]], Conj[ub[u]], db[v], db[w],
              Eps[i,j]
           ],

  "24a" -> Op[Wt[G["24a"][r,s,t,u,v,w]],
              L[r,i], L[s,j], eb[t], Conj[Q[u,k]], Conj[Q[v,l]], db[w],
              Eps[i,k], Eps[j,l]
           ],

  "24b" -> Op[Wt[G["24b"][r,s,t,u,v,w]],
              L[r,i], L[s,j], eb[t], Conj[Q[u,k]], Conj[Q[v,l]], db[w],
              Eps[i,j], Eps[k,l]
           ],

  "25a" -> Op[Wt[G["25a"][r,s,t,u,v,w]],
              L[r,i], L[s,j], Conj[L[t,k]], Conj[Q[u,l]], db[v], db[w],
              Eps[i,k], Eps[j,l]
           ],

  "25b" -> Op[Wt[G["25b"][r,s,t,u,v,w]],
              L[r,i], L[s,j], Conj[L[t,k]], Conj[Q[u,l]], db[v], db[w],
              Eps[i,j], Eps[k,l]
           ],

  "26"  -> Op[Wt[G["26"][r,s,t,u,v,w]],
              L[r,i], Conj[Q[s,j]], db[t], db[u], db[v], Conj[db[w]],
              Eps[i,j]
           ],

  "27"  -> Op[Wt[G["27"][r,s,t,u,v,w]],
              Conj[eb[r]], ub[s], Conj[ub[t]], db[u], db[v], db[w]
           ],

  "28"  -> Op[Wt[G["28"][r,s,t,u,v,w]],
              L[r,i], Conj[L[s,j]], Conj[eb[t]], db[u], db[v], db[w],
              Eps[i,j]
           ],

  "29"  -> Op[Wt[G["29"][r,s,t,u]],
              L[r,i], db[s], db[t], db[u], Conj[H[j]], Conj[H[k]], H[l],
              Eps[i,k], Eps[j,l]
           ],

  "30"  -> Op[Wt[G["30"][r,s,t,u]],
              L[r,i], Conj[Q[s,j]], Conj[Q[t,k]], ub[u], H[l], H[m], H[n],
              Eps[i,n], Eps[j,l], Eps[k,m]
           ],

  "31"  -> Op[Wt[G["31"][r,s,t,u,v,w]],
              Conj[eb[r]], Q[s,i], Conj[Q[t,j]], db[u], db[v], db[w],
              Eps[i,j]
           ],

  "32"  -> Op[Wt[G["32"][r,s,t,u,v,w]],
              L[r,i], Conj[Q[s,j]], Conj[Q[t,k]], Conj[Q[u,l]], Conj[ub[v]], db[w],
              Eps[i,k], Eps[j,l]
           ],

  "33"  -> Op[Wt[G["33"][r,s,t,u,v,w]],
              L[r,i], Q[s,j], ub[t], db[u], db[v], db[w],
              Eps[i,j]
           ],

  "34a" -> Op[Wt[G["34a"][r,s,t,u,v,w]],
              L[r,i], Conj[Q[s,j]], Conj[Q[t,k]], Q[u,l], db[v], db[w],
              Eps[i,j], Eps[k,l]
           ],

  "34b" -> Op[Wt[G["34b"][r,s,t,u,v,w]],
              L[r,i], Conj[Q[s,j]], Conj[Q[t,k]], Q[u,l], db[v], db[w],
              Eps[i,l], Eps[j,k]
           ],

  "35a" -> Op[Wt[G["35a"][r,s,t,u]],
              L[r,i], Conj[Q[s,j]], Conj[Q[t,k]], db[u], H[l], H[m], Conj[H[n]],
              Eps[i,j], Eps[k,l], Eps[m,n]
           ],

  "35b" -> Op[Wt[G["35b"][r,s,t,u]],
              L[r,i], Conj[Q[s,j]], Conj[Q[t,k]], db[u], H[l], H[m], Conj[H[n]],
              Eps[i,m], Eps[j,n], Eps[k,l]
           ],

  "35c" -> Op[Wt[G["35c"][r,s,t,u]],
              L[r,i], Conj[Q[s,j]], Conj[Q[t,k]], db[u], H[l], H[m], Conj[H[n]],
              Eps[i,m], Eps[j,k], Eps[l,n]
           ],

  "35d" -> Op[Wt[G["35d"][r,s,t,u]],
              L[r,i], Conj[Q[s,j]], Conj[Q[t,k]], db[u], H[l], H[m], Conj[H[n]],
              Eps[i,n], Eps[j,l], Eps[k,m]
           ],

  "36"  -> Op[Wt[G["36"][r,s,t,u]],
              L[r,i], ub[s], db[t], db[u], H[j], H[k], Conj[H[l]],
              Eps[i,k], Eps[j,l]
           ],

  "37"  -> Op[Wt[G["37"][r,s,t,u]],
              Conj[eb[r]], Conj[Q[s,i]], db[t], db[u], H[j], H[k], Conj[H[l]],
              Eps[i,k], Eps[j,l]
           ],

  "38"  -> Op[Wt[G["38"][r,s,t,u,v,w]],
              L[r,i], eb[s], Conj[eb[t]], Conj[Q[u,j]], db[v], db[w],
              Eps[i,j]
           ],

  "39"  -> Op[Wt[G["39"][r,s,t,u,v,w]],
              L[r,i], Conj[Q[s,j]], ub[t], Conj[ub[u]], db[v], db[w],
              Eps[i,j]
           ]

  |>;
