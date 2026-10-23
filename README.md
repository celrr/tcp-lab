# tcp-lab

Un protocolo de transporte fiable sobre UDP, escrito desde cero en Python
y probado en una red con retardo y pérdidas simuladas (tc netem + Docker).

## Hoja de ruta
- [ ] v0.1 Stop-and-wait
- [ ] v0.3 Go-Back-N / Selective Repeat + RTO adaptativo (RFC 6298)
- [ ] v0.6 Control de flujo + fast retransmit
- [ ] v0.8 Control de congestión Reno y CUBIC
- [ ] v0.9 Experimentos
- [ ] v1.0 Comparación con TCP real (iperf3, CUBIC vs BBR)

## Cómo reproducir
    cd netem && docker compose up -d --build
