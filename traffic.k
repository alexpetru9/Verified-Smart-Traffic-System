module TRAFFIC
  // 1. Define Colors (Syntax)
  syntax Color ::= "NS_GREEN" | "NS_YELLOW" | "EW_GREEN" | "EW_YELLOW" | "ALL_RED"
   
  // 2. Define the Result (SAFE or UNSAFE)
  syntax Result ::= "SAFE" | "UNSAFE"
   
  // 3. Define the verification command
  syntax Command ::= "check" "(" Color "," Color ")"

  // 4. Program Configuration
  configuration <k> $PGM:Command </k>

  // --- SAFETY RULES ---

  // Green -> Yellow is allowed (SAFE)
  rule check(NS_GREEN, NS_YELLOW) => SAFE
  rule check(EW_GREEN, EW_YELLOW) => SAFE

  // Yellow -> Red is allowed (SAFE)
  rule check(NS_YELLOW, ALL_RED) => SAFE
  rule check(EW_YELLOW, ALL_RED) => SAFE

  // Red -> Green is allowed (SAFE)
  rule check(ALL_RED, NS_GREEN) => SAFE
  rule check(ALL_RED, EW_GREEN) => SAFE

  // Any other combination (e.g., Green -> Red directly) has no rule, so it will not yield SAFE.
endmodule