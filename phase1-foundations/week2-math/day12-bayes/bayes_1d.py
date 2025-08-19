# Bayesian update for 1D Gaussian prior/likelihood.
# Run: `python bayes_1d.py`
def bayes_1d(mu_prior, var_prior, z, mu_meas, var_meas):
    var_post = 1.0 / (1.0/var_prior + 1.0/var_meas)
    mu_post = var_post * (mu_prior/var_prior + mu_meas/var_meas)
    return mu_post, var_post

if __name__ == "__main__":
    print(bayes_1d(0.0, 1.0, z=1.2, mu_meas=1.2, var_meas=0.25))
