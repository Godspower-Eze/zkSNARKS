# Simple Protocol

## Description

This is a simple protocol that proves to a verifier that the prover knows a polynomial by being able to get the same output as the verifier when evaluated using a value root `x`.

## Steps

- The Verifier chooses a random value of `x` and evaluates his polynomial locally
- Verifier gives `x` to the prover and asks to evaluate the polynomial in question
- Prover evaluates his polynomial at x and gives the result to the verifier
- Verifier checks if the local result is equal to the prover's result, and if so then the statement is proven with a high confidence

## Motivation

Given two arbitrary polynomials they can only intersect at most d points where d is the degree of the polynomial.
