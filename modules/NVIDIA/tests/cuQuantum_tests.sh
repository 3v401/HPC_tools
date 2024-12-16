# cuStatevec example:

export LD_LIBRARY_PATH=${CUQUANTUM_ROOT}/lib:${LD_LIBRARY_PATH}
nvcc statevec_example.cu -I${CUQUANTUM_ROOT}/include -L${CUQUANTUM_ROOT}/lib -lcustatevec -o statevec_example
./statevec_example

# tensorNet example (default, MPI auto, MPI):

nvcc tensornet_example.cu -I${CUQUANTUM_ROOT}/include -I${CUTENSOR_ROOT}/include -L${CUQUANTUM_ROOT}/lib -L${CUTENSOR_ROOT}/lib/12 -lcutensornet -lcutensor -o tensornet_example
./tensornet_example

nvcc tensornet_example_mpi_auto.cu -I${CUQUANTUM_ROOT}/include -I${CUTENSOR_ROOT}/include -I${MPI_PATH}/include -L${CUQUANTUM_ROOT}/lib -L${CUTENSOR_ROOT}/lib/12 -lcutensornet -lcutensor -L${MPI_PATH}/lib -lmpi -o tensornet_example_mpi_auto
./tensornet_example_mpi_auto

nvcc tensornet_example_mpi.cu -I${CUQUANTUM_ROOT}/include -I${CUTENSOR_ROOT}/include -I${MPI_PATH}/include -L${CUQUANTUM_ROOT}/lib -L${CUTENSOR_ROOT}/lib/12 -lcutensornet -lcutensor -L${MPI_PATH}/lib -lmpi -o tensornet_example_mpi
./tensornet_example_mpi

#cuDensityMat example:

nvcc operator_action_example.cpp -I${CUQUANTUM_ROOT}/include -I${CUTENSOR_ROOT}/include -L${CUQUANTUM_ROOT}/lib -L${CUTENSOR_ROOT}/lib/12 -lcudensitymat -lcutensor -o operator_action_example
./operator_action_example

nvcc operator_action_mpi_example.cpp -I${CUQUANTUM_ROOT}/include -I${CUTENSOR_ROOT}/include -I${MPI_PATH}/include -L${CUQUANTUM_ROOT}/lib -L${CUTENSOR_ROOT}/lib/12 -lcudensitymat -lcutensor -L${MPI_PATH}/lib -lmpi -o operator_action_mpi_example
./operator_action_mpi_example
