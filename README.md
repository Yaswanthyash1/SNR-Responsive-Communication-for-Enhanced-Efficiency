
ABSTRACT : 

Wireless communication systems face many challenges due to fluctuating channel conditions
which lead to variable error rates and require robust error management tactics. Normal Automatic Repeat Request (ARQ) methods suffer from high communication overhead and latency
and are very inefficient in handling retransmissions. Although traditional HARQ (Hybrid Automatic Repeat Request) is effective, its widespread use is limited by high implementation costs.
This underscores the need for adaptive systems that can dynamically respond to changing channel conditions based on Signal-to-Noise ratio (SNR) values. The proposed scheme switches
between ARQ, HARQ with Bose-Chaudhuri-Hocquenghem (BCH) codes , and HARQ with
turbo codes based on channel conditions during the transmission. Further, this scheme incorporates a selective soft combining technique by estimating SNR at the receiver end. The
main goal is to achieve the maximum possible throughput even at very low SNR values while
maintaining optimal complexity.



INTRODUCTION :

Error control mechanisms play a crucial role in reliable data transmission. It ensures the retransmission of data
packets that are found to be erroneous or lost during the transmission. The end-to-end transfer of data from
one application to another application involves several steps, each subject to errors along the way. Due to
the necessity of numerous retransmissions, standard Automatic Repeat Request (ARQ) schemes fall short of
adequately correcting all errors. Thus, we are leveraging the technology of hybrid ARQ, which integrates ARQ
with Forward Error Correction (FEC), for its enhanced efficiency in this context. However, this system
may not be necessary under good channel conditions. To address this, we are developing an adaptive approach
that adjusts to the varying needs of different channel conditions.

The proposed scheme enhances system efficiency by dynamically switching among ARQ, HARQ with Turbo
Codes, and HARQ with BCH codes, based on fluctuating SNR values. It introduces a novel mechanism for
selective soft combining of packets at the receiver end, based on current channel conditions. This approach
minimizes retransmissions by utilizing corrupted packets rather than discarding them. Selecting the appropriate
schemes at every stage of data transmission will undoubtedly result in significant throughput improvements
across all scenarios.


DESIGN AND IMPLIMENTATION :

The proposed method focuses on improving communication efficiency by developing an adaptive Hybrid Automatic Repeat Request (HARQ) scheme. This scheme dynamically adapts to different schemes based on the
real-time fluctuations in signal-to-noise ratio (SNR) values. When SNR is very low, it switches to robust turbo codes for error correction with HARQ. Conversely, when SNR is moderate to high, it employs HARQ with BCH codes of different code rates Notably, when the SNR reaches an extremely high value, the scheme strategically switches back to pure ARQ to maintain simplicity. The scheme operates in four states: Pure ARQ withGo-back-N, two enhanced BCH codes HARQ1(4599,3447)  and HARQ2(4599,2295), and an optimal state using HARQ with Turbo codes.

Below four steps are used in the design and implimentation . 

A. SNR Estimation Algorithm
B. Throughput of Different Schemes
C. Switching Scheme
D. Decision Making for Soft Combining at Receiver End

( detailed  information is in finalpdf ) 






