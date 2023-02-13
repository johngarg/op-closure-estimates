$Assumptions = hloop > 0 && loop > 0 && vev > 0 && \[CapitalLambda] > 0;

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

    (* If no rules have been applied successfully, return the initial state *)
    Block[{maybeNewState = Last /@ rulesAndStates, newState},
      newState = If[maybeNewState === {}, {start}, maybeNewState];
      {DeleteDuplicates[newState], rules, updatedEdgeList}
    ]
  ];

ApplyRules[{x_Op, y___}, rules_, edgeList_] :=
  Block[
    {result, newStart, newEdgeList},

    result = Map[ApplyRules[#, rules, edgeList] &, {x, y}];
    newStart = Join @@ First /@ result;
    newEdgeList = DeleteDuplicates[Join @@ Last /@ result];
    {DeleteDuplicates[newStart], rules, newEdgeList}
  ];

ApplyRules[{}, rules_, edgeList_] := {{}, rules, edgeList};

ApplyRules[start_, rules_, edgeList_, n_] :=
  Nest[Apply[ApplyRules, #] &, {start, rules, edgeList}, n];


(* ToStringRep[db[r_, a_]] := *)
(*   ToString@StringForm["\!\(\\*SuperscriptBox[SubscriptBox[OverscriptBox[\(d\), \(_\)], \ \(`1`\)], \(`2`\)]\)", r, a]; *)

(* ToStringRep[ub[r_, a_]] := *)
(*   ToString@StringForm["\!\(\\*SuperscriptBox[SubscriptBox[OverscriptBox[\(u\), \(_\)], \ \(`1`\)], \(`2`\)]\)", r, a]; *)

ToStringRep[db[r_]] :=
  ToString@StringForm["\!\(\*SubscriptBox[OverscriptBox[\(d\), \(_\)], \(`1`\)]\)", r];

ToStringRep[ub[r_]] :=
  ToString@StringForm["\!\(\*SubscriptBox[OverscriptBox[\(u\), \(_\)], \(`1`\)]\)", r];

ToStringRep[eb[r_]] :=
  ToString@StringForm["\!\(\*SubscriptBox[OverscriptBox[\(e\), \(_\)], \(`1`\)]\)", r];

ToStringRep[L[r_, i_]] :=
  ToString@StringForm["\!\(\*SuperscriptBox[SubscriptBox[\(L\), \(`1`\)], \(`2`\)]\)", r, i];

ToStringRep[Q[r_, i_]] :=
  ToString@StringForm["\!\(\*SuperscriptBox[SubscriptBox[\(Q\), \(`1`\)], \(`2`\)]\)", r, i];

(* ToStringRep[Q[r_, a_, i_]] := *)
(*   ToString@StringForm[ *)
(*     "\!\(\\*SuperscriptBox[SubscriptBox[\(Q\), \(`1`\)], \(`2`\\\ \ `3`\)]\)", r, a, i]; *)

ToStringRep[H[i_]] :=
  ToString@StringForm["\!\(\*SuperscriptBox[\(H\), \(`1`\)]\)", i];

ToStringRep[Conj[x_]] :=
  StringJoin["\!\(\*SuperscriptBox[\(", ToStringRep[x], "\), \(\[Dagger]\)]\)"];

ToStringRep[Delta[i_, j_]] :=
  ToString@StringForm["\!\(\*SubscriptBox[\(\[Delta]\), \(`1`\\\ `2`\)]\)", i, j];

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
    (Op[name] @@ flavourList) (Select[matchedExpr, Head[#] == Wt &] /. Wt -> Identity /. Op -> Times) (* /. flavourRelabellings *)
  ];


MatchOperator[op_Op, rules_, n_] := ApplyRules[op, rules, {}, n];

RawMatchingData[graph_] :=
  DeleteDuplicates[
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
  ];

Conj[x_ y_] := Conj[x] Conj[y];
Conj[x_Ru] := Conjugate[x];
Conj[x_Rd] := Conjugate[x];
Conj[x_Rl] := Conjugate[x];
Conj[x_Lu] := Conjugate[x];
Conj[x_Ld] := Conjugate[x];
Conj[x_Ll] := Conjugate[x];


MaybeMakePattern[x_Integer] := x;
MaybeMakePattern[x_Symbol] := $pattern[x, Blank[]];

ChooseFlavour::usage = "Transforms `Op` matching expression to have flavour
indices given by `flavour` list. Can also be applied after
`CleanMatchingExpressionAndMakeRule`.";
ChooseFlavour[expr_Op, flavour_List] :=
  Block[
    {label, flavourIndices, flavourReplacements},

    flavourIndices = expr /. Op[x___, G[lab_][flav__], z___] :> List[flav];

    expr /. MapThread[Rule, {flavourIndices, flavour}]

  ];

ChooseFlavour[
  Rule[lhs : Op[leftlabel_String][leftidx__],
       rhs : Times[before___, G[smeftlabel_String][smeftidx__], after___]],
  flavour_List
] :=
  Block[
    {rule = MapThread[Rule, {List[smeftidx], flavour}]},

    Rule @@ {
      lhs /. rule /. pat_[index_Integer, Blank[]] :> index,
      rhs /. rule
    }

  ];

(* Same as above but with `Conjugate` in argument. TODO Refactor to avoid
repetition. *)
ChooseFlavour[
  Rule[lhs : Op[leftlabel_String][leftidx__],
       rhs : Times[before___, Conjugate[G[smeftlabel_String][smeftidx__]], after___]],
  flavour_List
] :=
  Block[
    {rule = MapThread[Rule, {List[smeftidx], flavour}]},

    Rule @@ {
      lhs /. rule /. pat_[index_Integer, Blank[]] :> index,
      rhs /. rule
    }

  ];

ChooseFlavour[
  List[
    r: Rule[lhs : Op[leftlabel_String][leftidx__],
            rhs : Times[before___, G[smeftlabel_String][smeftidx__], after___]]
  ],
  flavour_List
] := ChooseFlavour[r, flavour];

ChooseFlavour[
  r: Rule[lhs : Op[leftlabel_String][leftidx__],
          rhs : x_Plus
     ],
  flavour_List
] :=
  Block[{splitUp, flavoured, stitchedUp},
        splitUp = Rule @@ {lhs, #} & /@ (List @@ x);
        flavoured = ChooseFlavour[#, flavour] & /@ splitUp;
        stitchedUp = Rule @@ {flavoured[[1]][[1]], Sum[pair[[2]], {pair, flavoured}]}
  ];


ExpandYukSums::usage = "Function to expand sums of indices that are repeated but
not present in any operator coefficient. (They come from rotating the fields
into the mass basis.) These indices are marked with names like \"yuk197\",
etc.";
ExpandYukSums[expr_] :=
  Block[{replaced, indices, sumHelper, sum$},
        replaced =
        ReplaceList[
          expr, {Times[x___, CKM[idx__], y___] :> List[idx],
                 Times[x___, Conjugate[CKM[idx__]], y___] :> List[idx]}];
        indices =
        DeleteDuplicates[
          Select[Flatten[replaced],
                 With[{s = ToString[#]},
                      StringLength[s] >= 4 && StringTake[s, 3] === "yuk"] &]];

        If[
          indices === {},
          expr,
          sumHelper =
          sum$[expr, Sequence @@ Table[{idx, 3}, {idx, indices}]];
          sumHelper /. sum$ -> Sum
        ]
  ];

ApplyExpandYukSums[op_ -> rhs_] := op -> ExpandYukSums[rhs];


CleanMatchingExpressionAndMakeRule::usage = "Makes summed variables look nice, turns
matching expressions into rules mapping WET to SMEFT operator expressions";
CleanMatchingExpressionAndMakeRule[
  Times[x___, smeftOp : G[n_][flavSMEFT__], leftOp : Op[label_String][flavLEFT__] | Conj[Op[label_String][flavLEFT__]], y___]
] :=
  Module[
    {indices, toRelabel, safeIndices, relabellings, func, rhs, result},

    indices = Select[List[flavLEFT], Head[#] === Symbol &];
    toRelabel = Select[indices, ! MemberQ[$DummyIndexList, #] &];
    safeIndices = Select[$DummyIndexList, ! MemberQ[indices, #] &];

    relabellings =
    MapThread[
      Rule,
      {toRelabel, Take[safeIndices, Length[toRelabel]]}
    ];

    func = If[Head[leftOp] === Conj, Conjugate, Identity];
    rhs = Refine[func /@ Times[x, smeftOp, y]];

    result =
    {(Op[label] @@ (MaybeMakePattern /@ List[flavLEFT]) /. $pattern -> Pattern) -> rhs /. relabellings};

    ApplyExpandYukSums /@ result

  ];

CleanMatchingExpressionAndMakeRule[x_Op] :=
  CleanMatchingExpressionAndMakeRule[(x /. Op[y__] :> Times[y])];

ToMassBasis = {
        Times[x___, ye[r_, s_], y___] :> (Times[ye[r], x, y] /. s -> r),
        Times[x___, yu[r_, s_], y___] :> (Times[yu[r], x, y] /. s -> r),
        yd[r_, s_] :> yd[r] Conjugate[CKM[r, s]],

        Times[x___, Conj[ye[r_, s_]],
              y___] :> (Times[ye[r], x, y] /. s -> r),
        Times[x___, Conj[yu[r_, s_]],
              y___] :> (Times[yu[r], x, y] /. s -> r),
        Conj[yd[r_, s_]] :> yd[r] CKM[r, s] (* FIXME Not 100% sure about whether
        the indices here should be transposed *)

};

ExtractMatchingData[data_] := RawMatchingData @ MultiwayGraph @ data;

ApplyFlavourAndMakeRule[rawData_, flavour_] :=
 ChooseFlavour[#, flavour] & /@ (Join @@
    CleanMatchingExpressionAndMakeRule /@ (rawData //. ToMassBasis));

GuidedMatchingDim9[opLabel_String] :=
        Block[{first, second, third, fourth},
              first = ApplyRules[BViolatingOperatorsDim9[opLabel], Join[YukawaRules, LoopRules], {}, 2];
              second = Apply[ApplyRules[#1, Join[EpsDeltaRules, FlavourDeltaRules], #3, 2] &, first];
              third = Apply[ApplyRules[#1, Join[DerivativeRules], #3, 1] &, second];
              Apply[ApplyRules[#1, OperatorMatchingRulesDim7, #3, 1] &, third]
        ];

MatchingDataDim8[opLabel_, flavour_] :=
        Block[{d8ex = EchoTiming @ MatchOperator[BViolatingOperatorsDim8[opLabel], $MatchingRulesDim8, 4]},
              ApplyFlavourAndMakeRule[ExtractMatchingData[d8ex], flavour] // DeleteDuplicates
        ];

MatchingDataDim9[opLabel_, flavour_] :=
        Block[{d9ex = EchoTiming @ GuidedMatchingDim9[opLabel]},
              ApplyFlavourAndMakeRule[ExtractMatchingData[d9ex], flavour] // DeleteDuplicates
        ];

$NFlavours = 3;
TreeLevelMatching = {
        (* Delta B = - Delta L *)
        G["~^S,LL_udd"][p_, q_, r_, s_] :> -2 Sum[CKM[q, qp] CKM[r, rp] 1/2 (Op["1"][p, qp, rp, s] + Op["1"][qp, p, rp, s]), {qp, $NFlavours}, {rp, $NFlavours}],
        G["~^S,LL_duu"][p_, q_, r_, s_] :> -2 Sum[CKM[p, pp] 1/2 (Op["1"][pp, q, r, s] + Op["1"][q, pp, r, s]), {pp, $NFlavours}],
        G["~^S,LR_duu"][p_, q_, r_, s_] :> -2 Sum[CKM[p, pp] 1/2 (Op["2"][pp, q, r, s] + Op["2"][q, pp, r, s]), {pp, $NFlavours}],
        G["~^S,RL_duu"][p_, q_, r_, s_] :> Op["4"][p, q, r, s],
        G["~^S,RL_dud"][p_, q_, r_, s_] :> -Sum[CKM[r, rp] Op["4"][p, q, rp, s], {rp, $NFlavours}],
        G["~^S,RL_ddu"][p_, q_, r_, s_] :> 1/2 (Op["11"][p, q, r, s] - Op["11"][q, p, r, s]) M["vev"]^2/(2 M["\[CapitalLambda]"]^2),
        G["~^S,RR_duu"][p_, q_, r_, s_] :> Op["3"][p, q, r, s],

        (* Delta B = - Delta L *)
        G["~^S,LL_ddd"][p_, q_, r_, s_] :> Op["?"][],
        G["~^S,LR_udd"][p_, q_, r_, s_] :> -(Op["6a"][q, p, s, r] + Conj[Op["6b"][p, q, s, r]] + Conj[Op["6b"][q, p, s, r]]) M["vev"]/(Sqrt[2] M["\[CapitalLambda]"]),
        G["~^S,LR_ddu"][p_, q_, r_, s_] :> Op["?"][],
        G["~^S,LR_ddd"][p_, q_, r_, s_] :> Conj[Op["6a"][p, q, s, r]] M["vev"]/(Sqrt[2] M["\[CapitalLambda]"]),
        G["~^S,RL_ddd"][p_, q_, r_, s_] :> 1/2 (Conj[Op["7"][p, q, s, r]] - Conj[Op["7"][q, p, s, r]]) M["vev"]/(Sqrt[2] M["\[CapitalLambda]"]),
        G["~^S,RR_udd"][p_, q_, r_, s_] :> - 1/2 (Conj[Op["8"][q, s, p, r]] - Conj[Op["8"][s, q, p, r]]) M["vev"]/(2 Sqrt[2] M["\[CapitalLambda]"]),
        G["~^S,RR_ddd"][p_, q_, r_, s_] :> - 1/2 (Conj[Op["5"][p, q, s, r]] - Conj[Op["5"][q, p, s, r]]) M["vev"]/(Sqrt[2] M["\[CapitalLambda]"])

};

MatchingData[label_, flavour_] :=
        If[MemberQ[Keys[BViolatingOperatorsDim8], label],
           MatchingDataDim8[label, flavour],
           MatchingDataDim9[label, flavour]
        ];


NumericReplacements =
Join[
        LatticeReplacements,
        NumericValues,
        {loop -> 1/(16 \[Pi]^2), hloop -> (1/(16 \[Pi]^2) + M["vev"]^2/(2 M["\[CapitalLambda]"]^2))}
];

NucleonDecays[label_String, flavour_List, "Symbolic"] :=
        Block[{expr, matching},
              matching = MatchingData[label, flavour];
              NucleonDecaysWithMatchingData[label, matching, "Symbolic"]
        ];

NucleonDecays[label_String, flavour_List, "Numeric"] :=
        NucleonDecays[label, flavour, "Symbolic"] //. NumericReplacements;

NucleonDecays[label_String, flavour_List] :=
        NucleonDecays[label, flavour, "Numeric"];

NucleonDecaysWithMatchingData[label_String, matching_, "Symbolic"] :=
        Block[{expr},
              Table[
                      expr = LatticeNucleonDecayExpression[proc];
                      proc -> expr //. Join[MatElemReplacements] /. TreeLevelMatching /. matching /. Op[x_][y___] :> 0 /. Conj -> Conjugate,
                      {proc,  If[MemberQ[Keys[BViolatingOperatorsDim8], label],
                                 ProtonDecayProcessesDim6,
                                 ProtonDecayProcessesDim7
                              ]
                      }
              ]
        ];

NucleonDecaysWithMatchingData[label_String, matching_, "Numeric"] :=
        NucleonDecaysWithMatchingData[label, matching, "Symbolic"] //. NumericReplacements;

NucleonDecaysWithMatchingData[label_String, matching_] :=
        NucleonDecaysWithMatchingData[label, matching, "Numeric"]


ExtractDominantMatchingByRate[] := $NotImplemented;







WriteMatchingData::usage = "Write the matching data with general flavour
indices.";
WriteMatchingData[label_String, path_String] :=
  Block[
    {matchingData, data, filepath},

    matchingData = MatchingData[label];
    Table[
      data = CleanMatchingExpressionAndMakeRule /@ matchingData;
      filepath = path <> "op" <> label <> ".dat";
      Export[filepath, data];
      (* TODO Only print this when Export works *)
      Print[filepath <> " written!"];
    ]
  ];


NucleonDecayMatchingData::usage = "Uses the matching data to match against
operators that contribute to nucleon decays. Flavour structure is optional.";
NucleonDecayMatchingData[data_] :=
  Block[
    {operatorsForNucleonDecay, groupedContributions, cleanContributions},

    operatorsForNucleonDecay = Flatten[Values[ProcessToWETTable] /. Plus -> List] /. G -> Op;

    (* For each operator that contributes to nucleon decay, run a replace list
    to get all possible matches, then group these by the operator to get all
    contributions to the same operator coefficient. *)
    groupedContributions = Normal[GroupBy[# -> ReplaceList[#, data] & /@ operatorsForNucleonDecay, First]];

    (* Then, delete duplicates by absolute value (we can't account for
    cancellations) and remove additional structure introduced from GroupBy call.
    Also remove empty lists from unmatched coefficients. *)
    cleanContributions =
    Select[
      #[[1]] -> DeleteDuplicatesBy[Join @@ Map[Last, #[[2]]], Abs] & /@ groupedContributions,
      ! Last[#] === {} &
    ];

    DeleteDuplicatesBy[cleanContributions, Abs]

  ];

NucleonDecayMatchingData[data_, flavour_] :=
  Block[
    {flavouredData},

    (* Impose the specified flavour structure on the data *)
    flavouredData = ChooseFlavour[#, flavour] & /@ data;

    NucleonDecayMatchingData[flavouredData]

  ];



ExtractDominantMatchingByOperator::usage = "Returns a replacement list mapping
each LEFT coefficient that is generated and contributes to nucleon decay to the
dominant symbolic expressions. `data` is a replacement list like:

{Op[\"^S,LL_duu\"][x_, 1, 1, 1] -> loop^2 CKM[2, x] yu[1] yu[2] G[\"9\"][1, 1, 1, 2],
 Op[\"^S,LL_duu\"][x_, 1, 2, 1] -> -loop^2 CKM[1, x] yu[1] yu[2] G[\"9\"][1, 1, 1, 2],
 ...
}.

That is, the output of `WriteMatchingData`.

We don't want to draw significance to any cancellations, so this is the main
function to use, not `NucleonDecayMatchingData`.";
ExtractDominantMatchingByOperator[data_, flavour_] :=
  Block[
    {numericReplacements, maximumContributions, withNumericValue,
    cleanContributions},

    cleanContributions = NucleonDecayMatchingData[data, flavour];

    numericReplacements =
    {loop -> 1/(16 \[Pi]^2)}~Join~NumericValues;

    (* For each of these, just take the maximum by numeric value *)
    maximumContributions =
    Table[
      (First[row] /. Op -> G) ->
      First[
        MaximalBy[Abs[Last[row]], Abs[#] /. G[x_][y__] :> 1 /. numericReplacements &]
      ],
      {row, cleanContributions}
    ];

    (* Decided not to return both the analytic and the numerical value here... *)
    (* withNumericValue = #[[1]] -> <| "Analytic" -> #[[2]], "Numerical" -> Abs[#[[2]]] /. numericReplacements |> & /@ maximumContributions; *)
    ReverseSortBy[maximumContributions, Abs[Last[#]] /. G[x_][y__] :> 1 /. numericReplacements &]

  ];

ProtonDecayRates[data_, flavour_] :=
  Block[
    {operatorsForNucleonDecay, protonDecayExpressions},

    operatorsForNucleonDecay =
    Flatten[Values[ProcessToWETTable] /. Plus -> List];

    (* Introduce legacy tilde; mark LEFT operator coefficients *)
    matchingData =
    Table[
      (rule[[1]] /. G[x_String][y__] :> GLEFT["~"<>x][y]) -> rule[[2]],
      {rule, ExtractDominantMatchingByOperator[data, flavour]}
    ];

    protonDecayExpressions = Table[
      proc -> LatticeNucleonDecayExpression[proc],
      {proc, ProtonDecayProcesses}
    ];

    protonDecayExpressions = protonDecayExpressions /. G -> GLEFT /. matchingData;

    protonDecayExpressions /. matchingData /. GLEFT[x_][y__] :> 0

  ];

ProtonDecayRates[data_, flavour_, "Numeric"] :=
  Block[
    {replacements},

    replacements
    = Join[MatElemReplacements, LatticeReplacements, NumericValues, {loop -> 1/(16 \[Pi]^2)}];

    ProtonDecayRates[data, flavour] //. replacements
  ];

ExtractDominantMatchingByRate::usage = "Returns a replacement list mapping each
nucleon decay process that is generated to a numerical expression that
dominantes the nucleon decay limit. This is useful for the final table.";
ExtractDominantMatchingByRate[data_] := $NotImplemented;
