import math


def newton_method(f, df, x0, tol=1e-10, max_iter=100):
    """Trouve une racine de f(x)=0 par la méthode de Newton.

    f : fonction
    df : dérivée de f
    x0 : point de départ
    tol : tolérance sur l’erreur
    max_iter : nombre maximal d’itérations
    """
    x = x0
    for i in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ZeroDivisionError(f"Dérivée nulle en x={x}, Newton échoue")
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError(f"Newton n'a pas convergé après {max_iter} itérations")


def trapezoidal_rule(f, a, b, n=1000):
    """Intégrale de f entre a et b par la méthode du trapèze avec n sous-intervalles."""
    if n <= 0:
        raise ValueError("n doit être un entier positif")
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for k in range(1, n):
        s += f(a + k * h)
    return s * h


if __name__ == "__main__":
    # Exemple : racine de f(x)=x^2-2 (on espère sqrt(2))
    f = lambda x: x * x - 2
    df = lambda x: 2 * x
    racine = newton_method(f, df, x0=1.0, tol=1e-12, max_iter=50)
    print(f"Newton : racine approximative de x^2-2 = {racine:.12f} (vrai sqrt(2)={math.sqrt(2):.12f})")

    # Exemple : integral de sin(x) entre 0 et pi (valeur 2)
    g = math.sin
    integral = trapezoidal_rule(g, 0.0, math.pi, n=10000)
    print(f"Trapèze : integral de sin entre 0 et pi ≈ {integral:.12f} (vrai = 2)")
