import hifive
import numpy as np
import matplotlib.pyplot as plt
hic=hifive.HiC('/Users/xiangning/qbb2020-answers/HW9/project_step3', 'r')
data = hic.cis_heatmap('chr13', 1000000, datatype='fend', arraytype='full', diagonalincluded=True)
enrichment = data[:, :, 0] / data[:, :, 1]
inds = np.where(np.isnan(enrichment))
enrichment[inds] = 1
print("The shape of the data is ",data.shape)

# #Plotting 

plt.rcParams["figure.figsize"] = (10,10)
plt.imshow(np.log2(enrichment))
plt.title('enrichment_heatmap')
plt.savefig('enrichment_heatmap.png')



##Compartment analysis--Part I

plt.rcParams["figure.figsize"] = (20,3)
Comp = hifive.hic_domains.Compartment(hic, 100000, chroms=['chr13'], out_fname='tmp.hdf5')
Comp.write_eigen_scores('hic_comp.bed')
print(Comp)
X = Comp.positions['chr13']
Y = Comp.eigenv['chr13']
plt.plot(X,Y)
plt.xlabel('position')
plt.ylabel('compartment scores')
plt.savefig("compartment_score.png")

