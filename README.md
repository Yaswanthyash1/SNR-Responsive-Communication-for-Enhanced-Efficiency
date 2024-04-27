
## ABSTRACT : 

Wireless communication systems face many challenges due to fluctuating channel conditions
which lead to variable error rates and require robust error management tactics. Normal Automatic Repeat Request (ARQ) methods suffer from high communication overhead and latency
and are very inefficient in handling retransmissions. Although traditional HARQ (Hybrid Automatic Repeat Request) is effective, its widespread use is limited by high implementation costs.
This underscores the need for adaptive systems that can dynamically respond to changing channel conditions based on Signal-to-Noise ratio (SNR) values. The proposed scheme switches
between ARQ, HARQ with Bose-Chaudhuri-Hocquenghem (BCH) codes , and HARQ with
turbo codes based on channel conditions during the transmission. Further, this scheme incorporates a selective soft combining technique by estimating SNR at the receiver end. The
main goal is to achieve the maximum possible throughput even at very low SNR values while
maintaining optimal complexity.



## INTRODUCTION :

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


## DESIGN AND IMPLIMENTATION :

The proposed method focuses on improving communication efficiency by developing an adaptive Hybrid Automatic Repeat Request (HARQ) scheme. This scheme dynamically adapts to different schemes based on the
real-time fluctuations in signal-to-noise ratio (SNR) values. When SNR is very low, it switches to robust turbo codes for error correction with HARQ. Conversely, when SNR is moderate to high, it employs HARQ with BCH codes of different code rates Notably, when the SNR reaches an extremely high value, the scheme strategically switches back to pure ARQ to maintain simplicity. The scheme operates in four states: Pure ARQ withGo-back-N, two enhanced BCH codes HARQ1(4599,3447)  and HARQ2(4599,2295), and an optimal state using HARQ with Turbo codes.

Below four steps are used in the design and implimentation . 

- ### SNR Estimation Algorithm
- ### Throughput of Different Schemes
- ### Switching Scheme
- ### Decision Making for Soft Combining at Receiver End

( detailed  information is in final.pdf ) 

## RESULTS & ANALYSIS

### Transitions between various HARQ and ARQ schemes : 
![Screenshot 2024-03-14 161922](https://github.com/Yaswanthyash1/SNR-Responsive-Communication-for-Enhanced-Efficiency/assets/147232443/dbcb996d-a0e6-47cf-8fbe-1dcf83da9a02)

###  Estimated Throughput vs SNR for HARQ with Turbo codes (code rate = 1/3) :

![Turbo](https://github.com/Yaswanthyash1/SNR-Responsive-Communication-for-Enhanced-Efficiency/assets/147232443/65bebe28-ff97-46fe-ad55-a1749b189b7b)

### Performance comparision with and without Softcombing :
![Screenshot 2024-03-14 210836](https://github.com/Yaswanthyash1/SNR-Responsive-Communication-for-Enhanced-Efficiency/assets/147232443/fd0caaeb-e60c-4002-a2c3-815f10764734)

### Decoding Time vs SNR for Turbo Codes and BCH Codes : 
![Screenshot 2024-03-14 215739](https://github.com/Yaswanthyash1/SNR-Responsive-Communication-for-Enhanced-Efficiency/assets/147232443/f8a23ba4-388c-455e-b08a-3171152059de)



## CONCLUSION AND FUTURE WORKS 
In this paper, we have developed a SNR responsive scheme that switches between ARQ and HARQ using BCH
and turbo coding. Additionally, we’ve integrated a selective soft combining method for improved performance.
The strategic utilization of turbo codes under very low SNR conditions, coupled with BCH codes in other
scenarios, strikes an optimal balance between cost-effectiveness and reliability.As soft combining is selectively
avoided under good channel conditions, the associated complexity overhead is minimized and also improves
performance and maximizes throughput. The proposed scheme’s effectiveness is validated through simulation
results using turbo coding and selective soft combining. These results demonstrate a significant improvement
in throughput while also reducing complexity at every level of data transmission.
The simulations in this paper were conducted within the framework of the Land Mobile Satellite (LMS)  channel, specifically under rural conditions. Future work could involve extending these simulations to
other communication channels and determining thresholds through comprehensive simulations. Additionally,
simulations for thresholds in our paper are done in trail and error methods.this can be made more accurate by
leveraging Machine Learning and deep learning schemes.


<hr>

## "Suggestions and project improvement ideas are welcomed!"

## <bold>Thanks a lot,</bold><br/>

 Team members : 

 - C. Gnana Jyothi
-  P. Chandana Sai Sri Hasitha
-  N. Yaswanth
   

