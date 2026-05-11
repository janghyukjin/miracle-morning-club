// ============ 26주 LC + Tasks 데이터 (단일 진실 소스) ============
// 이 파일을 수정하면 index.html, checklist.html 모두 자동 반영됨.

const START_DATE = new Date(2026, 4, 8); // 2026-05-08 (금)

const WEEKS = [
  { n: 1, title: "Arrays & Hashing", topic: "주력 패턴 입문", problems: [
    { lc: "49", name: "Group Anagrams", diff: "M", slug: "group-anagrams" },
    { lc: "347", name: "Top K Frequent Elements", diff: "M", slug: "top-k-frequent-elements" },
    { lc: "238", name: "Product of Array Except Self", diff: "M", slug: "product-of-array-except-self" },
    { lc: "271", name: "Encode and Decode Strings", diff: "M", slug: "encode-and-decode-strings" },
    { lc: "128", name: "Longest Consecutive Sequence", diff: "M", slug: "longest-consecutive-sequence" },
    { lc: "11", name: "Container With Most Water", diff: "M", slug: "container-with-most-water" },
    { lc: "42", name: "Trapping Rain Water", diff: "H", slug: "trapping-rain-water" }
  ], tasks: ["본인 핵심 프로젝트 5분 영어 스크립트 작성", "주간 복습"] },

  { n: 2, title: "Sliding Window", topic: "약점 영역 1/4", problems: [
    { lc: "3", name: "Longest Substring Without Repeating Characters", diff: "M", slug: "longest-substring-without-repeating-characters" },
    { lc: "424", name: "Longest Repeating Character Replacement", diff: "M", slug: "longest-repeating-character-replacement" },
    { lc: "567", name: "Permutation in String", diff: "M", slug: "permutation-in-string" },
    { lc: "76", name: "Minimum Window Substring", diff: "H", slug: "minimum-window-substring" },
    { lc: "239", name: "Sliding Window Maximum", diff: "H", slug: "sliding-window-maximum" },
    { lc: "155", name: "Min Stack", diff: "M", slug: "min-stack" },
    { lc: "22", name: "Generate Parentheses", diff: "M", slug: "generate-parentheses" }
  ], tasks: ["면접 표현 50개 익히기", "주간 복습"] },

  { n: 3, title: "Binary Search + Stack", topic: "어려운 패턴", problems: [
    { lc: "704", name: "Binary Search", diff: "E", slug: "binary-search" },
    { lc: "74", name: "Search a 2D Matrix", diff: "M", slug: "search-a-2d-matrix" },
    { lc: "875", name: "Koko Eating Bananas", diff: "M", slug: "koko-eating-bananas" },
    { lc: "153", name: "Find Minimum in Rotated Sorted Array", diff: "M", slug: "find-minimum-in-rotated-sorted-array" },
    { lc: "33", name: "Search in Rotated Sorted Array", diff: "M", slug: "search-in-rotated-sorted-array" },
    { lc: "4", name: "Median of Two Sorted Arrays", diff: "H", slug: "median-of-two-sorted-arrays" },
    { lc: "853", name: "Car Fleet", diff: "M", slug: "car-fleet" },
    { lc: "84", name: "Largest Rectangle in Histogram", diff: "H", slug: "largest-rectangle-in-histogram" }
  ], tasks: ["본인 프로젝트 15분 영어 스크립트 시작", "ByteByteGo 영상 시청"] },

  { n: 4, title: "Linked List + 첫 모의 인터뷰", topic: "Phase 1 마무리", problems: [
    { lc: "143", name: "Reorder List", diff: "M", slug: "reorder-list" },
    { lc: "138", name: "Copy List with Random Pointer", diff: "M", slug: "copy-list-with-random-pointer" },
    { lc: "2", name: "Add Two Numbers", diff: "M", slug: "add-two-numbers" },
    { lc: "287", name: "Find the Duplicate Number", diff: "M", slug: "find-the-duplicate-number" },
    { lc: "146", name: "LRU Cache", diff: "M", slug: "lru-cache" },
    { lc: "23", name: "Merge k Sorted Lists", diff: "H", slug: "merge-k-sorted-lists" },
    { lc: "25", name: "Reverse Nodes in k-Group", diff: "H", slug: "reverse-nodes-in-k-group" }
  ], tasks: ["Pramp 첫 모의 인터뷰", "본인 프로젝트 15분 영어 발표 완성"] },

  { n: 5, title: "Trees 기초", topic: "Tree 패턴 1/2", problems: [
    { lc: "226", name: "Invert Binary Tree", diff: "E", slug: "invert-binary-tree" },
    { lc: "543", name: "Diameter of Binary Tree", diff: "E", slug: "diameter-of-binary-tree" },
    { lc: "110", name: "Balanced Binary Tree", diff: "E", slug: "balanced-binary-tree" },
    { lc: "100", name: "Same Tree", diff: "E", slug: "same-tree" },
    { lc: "572", name: "Subtree of Another Tree", diff: "E", slug: "subtree-of-another-tree" },
    { lc: "235", name: "Lowest Common Ancestor of a BST", diff: "M", slug: "lowest-common-ancestor-of-a-binary-search-tree" },
    { lc: "102", name: "Binary Tree Level Order Traversal", diff: "M", slug: "binary-tree-level-order-traversal" }
  ], tasks: ["STAR 답변 1번 (어려운 기술 문제)"] },

  { n: 6, title: "Trees 심화 + Tries", topic: "Tree 패턴 2/2", problems: [
    { lc: "199", name: "Binary Tree Right Side View", diff: "M", slug: "binary-tree-right-side-view" },
    { lc: "1448", name: "Count Good Nodes in Binary Tree", diff: "M", slug: "count-good-nodes-in-binary-tree" },
    { lc: "230", name: "Kth Smallest Element in a BST", diff: "M", slug: "kth-smallest-element-in-a-bst" },
    { lc: "124", name: "Binary Tree Maximum Path Sum", diff: "H", slug: "binary-tree-maximum-path-sum" },
    { lc: "297", name: "Serialize and Deserialize Binary Tree", diff: "H", slug: "serialize-and-deserialize-binary-tree" },
    { lc: "208", name: "Implement Trie (Prefix Tree)", diff: "M", slug: "implement-trie-prefix-tree" },
    { lc: "212", name: "Word Search II", diff: "H", slug: "word-search-ii" }
  ], tasks: ["STAR 답변 2번 (갈등 해결)"] },

  { n: 7, title: "Heap / Priority Queue", topic: "약점 영역 2/4", problems: [
    { lc: "703", name: "Kth Largest Element in a Stream", diff: "E", slug: "kth-largest-element-in-a-stream" },
    { lc: "1046", name: "Last Stone Weight", diff: "E", slug: "last-stone-weight" },
    { lc: "973", name: "K Closest Points to Origin", diff: "M", slug: "k-closest-points-to-origin" },
    { lc: "621", name: "Task Scheduler", diff: "M", slug: "task-scheduler" },
    { lc: "295", name: "Find Median from Data Stream", diff: "H", slug: "find-median-from-data-stream" }
  ], tasks: ["STAR 답변 3번 (리더십)", "Pramp 모의 1회"] },

  { n: 8, title: "Backtracking", topic: "재귀/탐색 마스터", problems: [
    { lc: "39", name: "Combination Sum", diff: "M", slug: "combination-sum" },
    { lc: "46", name: "Permutations", diff: "M", slug: "permutations" },
    { lc: "79", name: "Word Search", diff: "M", slug: "word-search" },
    { lc: "131", name: "Palindrome Partitioning", diff: "M", slug: "palindrome-partitioning" },
    { lc: "17", name: "Letter Combinations of a Phone Number", diff: "M", slug: "letter-combinations-of-a-phone-number" },
    { lc: "51", name: "N-Queens", diff: "H", slug: "n-queens" }
  ], tasks: ["STAR 답변 4번 (실패 경험)"] },

  { n: 9, title: "Graphs (BFS/DFS)", topic: "약점 영역 3/4 ⚠️", problems: [
    { lc: "200", name: "Number of Islands", diff: "M", slug: "number-of-islands" },
    { lc: "695", name: "Max Area of Island", diff: "M", slug: "max-area-of-island" },
    { lc: "133", name: "Clone Graph", diff: "M", slug: "clone-graph" },
    { lc: "994", name: "Rotting Oranges", diff: "M", slug: "rotting-oranges" },
    { lc: "207", name: "Course Schedule", diff: "M", slug: "course-schedule" },
    { lc: "210", name: "Course Schedule II", diff: "M", slug: "course-schedule-ii" },
    { lc: "417", name: "Pacific Atlantic Water Flow", diff: "M", slug: "pacific-atlantic-water-flow" }
  ], tasks: ["STAR 답변 5번 (영향력)", "System Design: Rate Limiter 시나리오"] },

  { n: 10, title: "Graphs Hard", topic: "약점 영역 마무리", problems: [
    { lc: "130", name: "Surrounded Regions", diff: "M", slug: "surrounded-regions" },
    { lc: "127", name: "Word Ladder", diff: "H", slug: "word-ladder" },
    { lc: "329", name: "Longest Increasing Path in a Matrix", diff: "H", slug: "longest-increasing-path-in-a-matrix" },
    { lc: "286", name: "Walls and Gates", diff: "M", slug: "walls-and-gates" },
    { lc: "261", name: "Graph Valid Tree", diff: "M", slug: "graph-valid-tree" },
    { lc: "323", name: "Number of Connected Components in an Undirected Graph", diff: "M", slug: "number-of-connected-components-in-an-undirected-graph" }
  ], tasks: ["Rate Limiter 영어 발표 녹음"] },

  { n: 11, title: "Advanced Graphs", topic: "Dijkstra/MST", problems: [
    { lc: "743", name: "Network Delay Time (Dijkstra)", diff: "M", slug: "network-delay-time" },
    { lc: "332", name: "Reconstruct Itinerary", diff: "H", slug: "reconstruct-itinerary" },
    { lc: "1584", name: "Min Cost to Connect All Points (MST)", diff: "M", slug: "min-cost-to-connect-all-points" },
    { lc: "787", name: "Cheapest Flights Within K Stops", diff: "M", slug: "cheapest-flights-within-k-stops" },
    { lc: "778", name: "Swim in Rising Water", diff: "H", slug: "swim-in-rising-water" }
  ], tasks: ["System Design: Distributed Cache 시나리오"] },

  { n: 12, title: "1D DP 시작", topic: "DP 입문", problems: [
    { lc: "213", name: "House Robber II", diff: "M", slug: "house-robber-ii" },
    { lc: "5", name: "Longest Palindromic Substring", diff: "M", slug: "longest-palindromic-substring" },
    { lc: "91", name: "Decode Ways", diff: "M", slug: "decode-ways" },
    { lc: "322", name: "Coin Change", diff: "M", slug: "coin-change" },
    { lc: "152", name: "Maximum Product Subarray", diff: "M", slug: "maximum-product-subarray" },
    { lc: "139", name: "Word Break", diff: "M", slug: "word-break" },
    { lc: "300", name: "Longest Increasing Subsequence", diff: "M", slug: "longest-increasing-subsequence" }
  ], tasks: ["URL Shortener 시나리오"] },

  { n: 13, title: "1D DP 마스터", topic: "DP 심화 1/2", problems: [
    { lc: "416", name: "Partition Equal Subset Sum", diff: "M", slug: "partition-equal-subset-sum" },
    { lc: "32", name: "Longest Valid Parentheses", diff: "H", slug: "longest-valid-parentheses" },
    { lc: "64", name: "Minimum Path Sum", diff: "M", slug: "minimum-path-sum" },
    { lc: "120", name: "Triangle", diff: "M", slug: "triangle" },
    { lc: "198", name: "House Robber 복습", diff: "M", slug: "house-robber" }
  ], tasks: ["본인 프로젝트 30분 영어 발표 작성"] },

  { n: 14, title: "1D DP 마무리", topic: "DP 추가 패턴", problems: [
    { lc: "877", name: "Stone Game", diff: "M", slug: "stone-game" },
    { lc: "1027", name: "Longest Arithmetic Subsequence", diff: "M", slug: "longest-arithmetic-subsequence" },
    { lc: "740", name: "Delete and Earn", diff: "M", slug: "delete-and-earn" },
    { lc: "542", name: "01 Matrix", diff: "M", slug: "01-matrix" }
  ], tasks: ["본인 프로젝트 30분 영어 발표 녹음"] },

  { n: 15, title: "2D DP 1/2", topic: "약점 영역 4/4", problems: [
    { lc: "62", name: "Unique Paths", diff: "M", slug: "unique-paths" },
    { lc: "1143", name: "Longest Common Subsequence", diff: "M", slug: "longest-common-subsequence" },
    { lc: "309", name: "Best Time to Buy/Sell Stock with Cooldown", diff: "M", slug: "best-time-to-buy-and-sell-stock-with-cooldown" },
    { lc: "518", name: "Coin Change II", diff: "M", slug: "coin-change-ii" },
    { lc: "494", name: "Target Sum", diff: "M", slug: "target-sum" }
  ], tasks: ["Distributed Inference 시나리오"] },

  { n: 16, title: "2D DP 2/2 (Hard)", topic: "Hard DP", problems: [
    { lc: "72", name: "Edit Distance", diff: "H", slug: "edit-distance" },
    { lc: "312", name: "Burst Balloons", diff: "H", slug: "burst-balloons" },
    { lc: "115", name: "Distinct Subsequences", diff: "H", slug: "distinct-subsequences" },
    { lc: "97", name: "Interleaving String", diff: "M", slug: "interleaving-string" }
  ], tasks: ["Pramp 주 2회 시작"] },

  { n: 17, title: "Greedy + Intervals", topic: "면접 빈출", problems: [
    { lc: "55", name: "Jump Game", diff: "M", slug: "jump-game" },
    { lc: "45", name: "Jump Game II", diff: "M", slug: "jump-game-ii" },
    { lc: "134", name: "Gas Station", diff: "M", slug: "gas-station" },
    { lc: "846", name: "Hand of Straights", diff: "M", slug: "hand-of-straights" },
    { lc: "1899", name: "Merge Triplets to Form Target", diff: "M", slug: "merge-triplets-to-form-target-triplet" },
    { lc: "57", name: "Insert Interval", diff: "M", slug: "insert-interval" },
    { lc: "56", name: "Merge Intervals", diff: "M", slug: "merge-intervals" }
  ], tasks: ["영문 이력서 정제 시작"] },

  { n: 18, title: "Intervals + Math", topic: "기타 패턴", problems: [
    { lc: "435", name: "Non-overlapping Intervals", diff: "M", slug: "non-overlapping-intervals" },
    { lc: "252", name: "Meeting Rooms", diff: "E", slug: "meeting-rooms" },
    { lc: "253", name: "Meeting Rooms II", diff: "M", slug: "meeting-rooms-ii" },
    { lc: "1851", name: "Minimum Interval to Include Each Query", diff: "H", slug: "minimum-interval-to-include-each-query" },
    { lc: "763", name: "Partition Labels", diff: "M", slug: "partition-labels" },
    { lc: "678", name: "Valid Parenthesis String", diff: "M", slug: "valid-parenthesis-string" }
  ], tasks: ["LinkedIn 영문화"] },

  { n: 19, title: "빅테크 빈출 Hard", topic: "Hard 집중", problems: [
    { lc: "329", name: "Longest Increasing Path Matrix (복습)", diff: "H", slug: "longest-increasing-path-in-a-matrix" },
    { lc: "588", name: "Design In-Memory File System", diff: "H", slug: "design-in-memory-file-system" },
    { lc: "212", name: "Word Search II (복습)", diff: "H", slug: "word-search-ii" },
    { lc: "2115", name: "Find All Possible Recipes", diff: "M", slug: "find-all-possible-recipes-from-given-supplies" },
    { lc: "84", name: "Largest Rectangle (복습)", diff: "H", slug: "largest-rectangle-in-histogram" },
    { lc: "1235", name: "Maximum Profit in Job Scheduling", diff: "H", slug: "maximum-profit-in-job-scheduling" }
  ], tasks: ["모의 onsite 시뮬레이션 1회"] },

  { n: 20, title: "Design 문제", topic: "Design 패턴", problems: [
    { lc: "146", name: "LRU Cache (복습)", diff: "M", slug: "lru-cache" },
    { lc: "460", name: "LFU Cache", diff: "H", slug: "lfu-cache" },
    { lc: "295", name: "Find Median from Data Stream", diff: "H", slug: "find-median-from-data-stream" },
    { lc: "380", name: "Insert Delete GetRandom O(1)", diff: "M", slug: "insert-delete-getrandom-o1" },
    { lc: "355", name: "Design Twitter", diff: "M", slug: "design-twitter" }
  ], tasks: ["모의 onsite 시뮬레이션 1회"] },

  { n: 21, title: "회사 태그 1/2", topic: "회사별 빈출 50/100", problems: [
    { lc: "TAG", name: "회사 태그 문제 1-7 (LC Premium)", diff: "M", slug: null },
    { lc: "TAG", name: "회사 태그 문제 8-14", diff: "M", slug: null }
  ], tasks: ["JD 키워드 매핑 영어 답변", "모의 onsite 시뮬레이션"] },

  { n: 22, title: "회사 태그 2/2", topic: "회사별 빈출 50/100", problems: [
    { lc: "TAG", name: "회사 태그 문제 15-21", diff: "M", slug: null },
    { lc: "TAG", name: "회사 태그 문제 22-28 (Hard 집중)", diff: "H", slug: null }
  ], tasks: ["모의 onsite 시뮬레이션", "최종 이력서 점검"] },

  { n: 23, title: "지원 시작", topic: "3-5개사 지원", problems: [
    { lc: "REVIEW", name: "이번주는 약점 영역 복습", diff: "M", slug: null }
  ], tasks: ["회사 1 지원", "회사 2 지원", "회사 3 지원"] },

  { n: 24, title: "인터뷰 진행", topic: "라운드 진행", problems: [
    { lc: "REVIEW", name: "어려웠던 문제 재풀이", diff: "M", slug: null }
  ], tasks: ["인터뷰 라운드 진행", "라운드별 즉시 복기"] },

  { n: 25, title: "약점 보강", topic: "Last-mile 보강", problems: [
    { lc: "REVIEW", name: "Heap / Graph / 2D DP 약점 보강", diff: "M", slug: null }
  ], tasks: ["인터뷰 진행", "약점 보강"] },

  { n: 26, title: "오퍼 협상 + 마무리", topic: "🎉 완주", problems: [
    { lc: "FINAL", name: "최종 인터뷰 마무리", diff: "M", slug: null }
  ], tasks: ["오퍼 협상", "다음 단계 계획"] }
];
