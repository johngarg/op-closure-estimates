ExtendIfConsistent::usage = "Extend frame with data if consistent";
ExtendIfConsistent[pattern_, data_, frame_] :=
        If[
                MemberQ[Keys[frame], pattern],
                PatternMatch[frame[pattern], data, frame],
                Append[frame, pattern -> data]
        ];


PatternMatch::usage = "Match pattern with data. Patterns are wrapped in a `P` head.
E.g.

In[1]:= PatternMatch[
 G[P[p], P[x], P[q], P[s]] loop Conjugate[CKM[P[r], P[x]]] yd[P[s]],
 G[p, x, q, r] loop Conjugate[CKM[s, x]] yd[r]
 ]

Out[1]= <|P[r] -> s, P[x] -> x, P[p] -> p, P[q] -> q, P[s] -> r|>

";

PatternMatch[pattern_, data_, False] := False;
PatternMatch[P[p_], data_, frame_] :=
  ExtendIfConsistent[P[p], data, frame];
PatternMatch[pattern_, pattern_, frame_] := frame;

PatternMatch[patts_List, datas_List, frame_] /;
Length[patts] == Length[datas] :=
        PatternMatch[
                Rest[patts], Rest[datas],
                PatternMatch[First[patts], First[datas], frame]
        ];

PatternMatch[patts_Times, datas_Times, frame_] :=
  PatternMatch[List @@ patts, List @@ datas, frame];

PatternMatch[f_[patts__], g_[datas__], frame_] /;
(! f === List) && (! False === PatternMatch[f, g, frame]) :=
        PatternMatch[{patts}, {datas}, frame];

PatternMatch[pattern_, data_, frame_] := False;

PatternMatch[pattern_, data_] := PatternMatch[pattern, data, <||>];
