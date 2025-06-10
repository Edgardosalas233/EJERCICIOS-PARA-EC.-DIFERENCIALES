const resultados = {
  ejercicio1: {
    euler: 59.0583,
    heun: 58.9050,
    rk4: 58.9506
  },
  ejercicio2: {
    euler: -31.3169,
    heun: -31.3157,
    rk4: -31.3157
  },
  ejercicio3: {
    euler: 4985.7409,
    heun: 4980.5022,
    rk4: 4981.7255
  }
};

window.onload = () => {
  for (let i = 1; i <= 3; i++) {
    const e = resultados[`ejercicio${i}`];
    document.getElementById(`res-e${i}`).textContent = e.euler.toFixed(4);
    document.getElementById(`res-h${i}`).textContent = e.heun.toFixed(4);
    document.getElementById(`res-r${i}`).textContent = e.rk4.toFixed(4);

    // También actualizamos la tabla comparativa
    document.getElementById(`comp-e${i}`).textContent = e.euler.toFixed(4);
    document.getElementById(`comp-h${i}`).textContent = e.heun.toFixed(4);
    document.getElementById(`comp-r${i}`).textContent = e.rk4.toFixed(4);
  }
};
