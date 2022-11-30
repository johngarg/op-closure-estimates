Op::usage = "An orderless collection of objects representing the state of the operator as the rules are applied.";
SetAttributes[Op, Orderless];

Op[x___, Power[y_, n_], z___] := Op[x, Sequence @@ Table[y, n], z];

Op[x___, Nothing, y___] := Op[x, y];


SetAttributes[Eps, Orderless];


MultiwayVertexFunction::usage = "Function to use to draw the nodes in the Multiway graph.";
MultiwayVertexFunction[{xc_, yc_}, name_, {w_, h_}] :=
  Module[{ruleQ, ruleColour},
         ruleQ = (Head[name] === List);
         ruleColour = If[ruleQ, Hue[0.09, 1, 0.91] , Hue[0.62, 0.45, 0.87]];
         Inset[
           Text[
             Framed[
               Style[
                 If[ruleQ, Text[RuleLabel[name[[2]]]] , ToStringRep[name]],
                 If[ruleQ, Hue[0.09, 1, 0.32] , Hue[0.62, 1, 0.48]]],
               Background -> Directive[Opacity[0.2], ruleColour],
               RoundingRadius -> 1,
               FrameStyle -> Directive[Opacity[0.5], ruleColour]]],
           {xc, yc}
         ]
  ];


MultiwayGraph::usage = "Draws a graph that visualises the possible proton decay chains.";
MultiwayGraph[{leaves_, rules_, edgeList_}] :=
  Graph[edgeList, VertexShapeFunction -> MultiwayVertexFunction, VertexSize -> 0.4, GraphLayout -> "LayeredDigraphEmbedding"];


MultiwayGraphHighlight::usage = "Highlights `n` paths in the Mutliway graph from `start` to `end`.";
MultiwayGraphHighlight[graph_, start_, end_, n_] :=
  HighlightGraph[graph, FindPath[graph, start, end, Infinity, n], GraphHighlightStyle -> "DehighlightFade"];

MultiwayGraphHighlight[graph_, start_, end_] :=
  MultiwayGraphHighlight[graph, start, end, 1];


MultiwayGraphWeights::usage = "Extract symbolic weights from `graph`.";

MultiwayGraphWeights[graph_] :=
  Map[# -> PropertyValue[{graph, #}, EdgeWeight]&, EdgeList[graph]];


MultiwayGraphRuleWeights::usage = "Extract symbolic weights from `graph` only for rules.";
MultiwayGraphRuleWeights[graph_] :=
  Select[MultiwayGraphWeights[graph], ListQ @* First];


ApplyRules::usage = "Apply `rules` once on `start` and update the edge list.";
ApplyRules[start_, rules_, edgeList_] :=
  Block[
    {rulesAndStates, startString, updatedEdgeList, fields, epsilons},

    startString = ToStringRep[start];
    (*Zip rules and final states together*)
    rulesAndStates =
    Partition[
      Flatten[
        Table[
          Block[
            {tuple, ruleApplications, vals, rulesWithCorrectVars},

            ruleApplications = ReplaceList[start, rule];
            vals = ruleApplications /. Op[x___, MatchingValues[y___]] :> List[y];
            rule = rule /. MatchingValues[x___] -> Nothing;
            ruleApplications = ruleApplications /. MatchingValues[x___] -> Nothing;

            rulesWithCorrectVars =
            Quiet[
              Table[
                rule /. Pattern -> First@*List /. Block[x_, y_] :> y /. (ToExpression[#[[1]]] -> #[[2]] & /@ val),
                {val, vals}
              ]
            ];

            MapThread[List, {rulesWithCorrectVars, ruleApplications}]
          ],
          {rule, rules}
        ]
      ],
      2];

    (*Updage edgeList to contain edge between start and applied rule*)
    updatedEdgeList = Join[edgeList, Table[start \[DirectedEdge] {start, $i[[1]]}, {$i, rulesAndStates}]];

    (*Updage edgeList to contain edge between rule and final state*)
    updatedEdgeList = Join[updatedEdgeList, Table[{start, $i[[1]]} \[DirectedEdge] $i[[2]], {$i, rulesAndStates}]];

    {Last /@ rulesAndStates, rules, updatedEdgeList}
  ];

ApplyRules[{x_Op, y___}, rules_, edgeList_] :=
  Block[
    {result, newStart, newEdgeList},

    result = ApplyRules[#, rules, edgeList] & /@ {x, y};
    newStart = Join @@ First /@ result;
    newEdgeList = DeleteDuplicates[Join @@ Last /@ result];
    {newStart, rules, newEdgeList}
  ];

ApplyRules[{}, rules_, edgeList_] := {{}, rules, edgeList};

ApplyRules[start_, rules_, edgeList_, n_] :=
  Nest[Apply[ApplyRules, #] &, {start, rules, edgeList}, n];


ToStringRep[db[r_, a_]] :=
  ToString@StringForm["\!\(\*SuperscriptBox[SubscriptBox[OverscriptBox[\(d\), \(_\)], \ \(`1`\)], \(`2`\)]\)", r, a];

ToStringRep[ub[r_, a_]] :=
  ToString@StringForm["\!\(\*SuperscriptBox[SubscriptBox[OverscriptBox[\(u\), \(_\)], \ \(`1`\)], \(`2`\)]\)", r, a];

ToStringRep[eb[r_]] :=
  ToString@StringForm["\!\(\*SubscriptBox[OverscriptBox[\(e\), \(_\)], \(`1`\)]\)", r];

ToStringRep[L[r_, i_]] :=
  ToString@StringForm["\!\(\*SuperscriptBox[SubscriptBox[\(L\), \(`1`\)], \(`2`\)]\)", r, i];

ToStringRep[Q[r_, a_, i_]] :=
  ToString@StringForm[
    "\!\(\*SuperscriptBox[SubscriptBox[\(Q\), \(`1`\)], \(`2`\\\ \ `3`\)]\)", r, a, i];

ToStringRep[H[i_]] :=
  ToString@StringForm["\!\(\*SuperscriptBox[\(H\), \(`1`\)]\)", i];

ToStringRep[Conj[x_]] :=
  StringJoin["\!\(\*SuperscriptBox[\(", ToStringRep[x], "\), \(\[Dagger]\)]\)"];

ToStringRep[Eps[i_, j_]] :=
  ToString@StringForm["\!\(\*SubscriptBox[\(\[Epsilon]\), \(`1`\\\ `2`\)]\)", i, j];

ToStringRep[Eps[a_, b_, c_]] :=
  ToString@StringForm[
    "\!\(\*SubscriptBox[\(\[Epsilon]\), \(`1`\\\ `2`\\\ `3`\)]\)", a, b, c];

ToStringRep[x_List] := StringJoin[Sort[ToStringRep /@ x]];

ToStringRep[Op[x___]] :=
  Block[
    {epsilons, fields, listx},

    listx = List[x];
    epsilons = Select[listx, Head[#] === Eps &];
    fields = Select[listx, ! Head[#] === Eps &];

    If[epsilons === {},
       ToStringRep[listx],
       ToStringRep[fields] <> "\n" <> ToStringRep[epsilons]
    ]
  ];

ToStringRep[Op[x_String][y__]] :=
  ToString[
    StringForm[
      "(\!\(\*SubscriptBox[\(O\), \(`1`\)]\)\!\(\*SubscriptBox[\()\), \ \(``\)]\)", x, StringJoin[ToString /@ List[y]]
    ]
  ];

ToStringRep[x_Wt] := "";
ToStringRep[x_MatchingValues] := "";
ToStringRep[x_Pattern] := "";
ToStringRep[rst] := "";
ToStringRep[rstWt] := "";
ToStringRep[rstMV] := "";
ToStringRep[G[x_][y__]] := ToString[G[x][y]];

ToStringRep[Deriv] := "\[PartialD]";


ToMath[loop] := 1/(16 \[Pi]^2);
ToMath[x_] := x;


RuleLabel[lhs_ :> rhs_] := ToStringRep[lhs] <> "\n \[Rule] " <> ToStringRep[rhs];


$DummyIndexList::usage = "Allowed indices to use as replacements."
$DummyIndexList = {x, y, z, w, xx, yy, zz, ww};


getFlavourRelabellings[x_List] :=
  Block[
    {indicesToRelabel},

    indicesToRelabel =
    If[StringSplit[ToString[#], _?LetterQ] === {}, Nothing, #] & /@ x;
    MapThread[
      Rule,
      {indicesToRelabel,
       Take[$DummyIndexList, Length[indicesToRelabel]]}]
  ];


makeMatchingExpr[{matchedExpr_, rule_RuleDelayed} \[DirectedEdge] Op[matchedOp : Op[name_][flavour__]]] :=
  Block[
    {flavourRelabellings, flavourList},

    flavourList = List[flavour];
    flavourRelabellings = getFlavourRelabellings[flavourList];
    (Op[name] @@ flavourList) (Select[matchedExpr, Head[#] == Wt &] /. Wt -> Identity /. Op -> Times) /. flavourRelabellings
  ];


MatchOperator[label_, n_] := ApplyRules[
   BViolatingOperatorsDim8[label],
   $MatchingRules,
   {},
   n];
MatchOperator[label_] := MatchOperator[label, 4];

MatchingData[graph_] := DeleteDuplicates[
  Block[{edgeList, matchedLeaves, matchedLeavesConj},
   edgeList = EdgeList[graph];
   matchedLeaves =
    Select[edgeList,
     MatchQ[#, _List \[DirectedEdge] Op[Op[_][___]]] &];
   matchedLeavesConj =
    Select[edgeList,
     MatchQ[#, _List \[DirectedEdge] Op[Conj[Op[_][___]]]] &];
   matchedLeaves = Join[matchedLeaves, matchedLeavesConj];
   makeMatchingExpr /@ matchedLeaves
   ]
  ]

Conj[x_ y_] := Conj[x] Conj[y];
Conj[x_Ru] := Conjugate[x];
Conj[x_Rd] := Conjugate[x];
Conj[x_Rl] := Conjugate[x];
Conj[x_Lu] := Conjugate[x];
Conj[x_Ld] := Conjugate[x];
Conj[x_Ll] := Conjugate[x];

MaybeMakePattern[x_Integer] := x;
MaybeMakePattern[x_Symbol] := $pattern[x, Blank[]];

ExportMatchingData[
  Times[x___, smeftOp : G[n_][flavSMEFT__],
   leftOp : Op[label_String][flavLEFT__], y___]] :=
 Block[{indices, toRelabel, safeIndices, relabellings},
  indices = Select[List[flavLEFT], Head[#] === Symbol &];
  toRelabel = Select[indices, ! MemberQ[$DummyIndexList, #] &];
  safeIndices = Select[$DummyIndexList, ! MemberQ[indices, #] &];
  relabellings =
   MapThread[
    Rule, {toRelabel, Take[safeIndices, Length[toRelabel]]}];
  {(Op[label] @@ (MaybeMakePattern /@ List[flavLEFT]) /. $pattern ->
        Pattern) -> Times[x, smeftOp, y] /. relabellings}
  ]
