import { setImmediate } from "node:timers";

function makeMatrix(n: number, fn: (i: number, j: number) => number): number[][] {
  const M: number[][] = []
  for (let i = 0; i < n; i++) {
    M[i] = []
    for (let j = 0; j < n; j++) M[i][j] = fn(i, j)
  }
  return M
}

async function main() {
  const N = 200
  const A = makeMatrix(N, (i, j) => i + j)
  const B = makeMatrix(N, (i, j) => i - j)
  const C: number[][] = Array.from({ length: N }, () => Array(N).fill(0))
  for (let i = 0; i < N; i++) {
    for (let k = 0; k < N; k++) {
      const aik = A[i][k]
      for (let j = 0; j < N; j++) C[i][j] += aik * B[k][j]
    }
  }
  await new Promise<void>((resolve) => setImmediate(resolve))
  console.log(C[0][0])
}

main().catch((err) => {
  console.error("Error:", err)
  process.exit(1)
})
