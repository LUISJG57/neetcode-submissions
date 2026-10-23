class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        conteo = {}
        maximo = 0
        while r < len(s):
            conteo[s[r]] = conteo.get(s[r], 0) + 1

            # si necesito más de k reemplazos, encojo desde la izquierda
            while (r - l + 1) - max(conteo.values()) > k:
                conteo[s[l]] -= 1
                l += 1

            maximo = max(maximo, r - l + 1)
            r += 1
        return maximo