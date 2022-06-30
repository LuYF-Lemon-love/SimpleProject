#include <stdio.h>
#include <pthread.h>

long double pi = 0.0;
long long items_num;
int threads_num;
pthread_mutex_t mut;

void * compute_pi(void * arg){
    
    int id = *(int *)arg;
    long long i;
    long long piece = items_num / threads_num;
    long long start = id * piece;
    long long end = start + piece;
    long double local_pi = 0.0;
    long double factor;
    
    if (start % 2 == 0)
        factor = 1.0;
    else
        factor = -1.0;
    
    for(i = start; i < end; i++, factor = -factor){
        local_pi += factor / (2 * i + 1);
    }

    pthread_mutex_lock(&mut);
    pi += 4.0 * local_pi;
    pthread_mutex_unlock(&mut);

    return NULL;
}

long double compute_pi_c(long long items, int threads){

    //printf("请耐心等待...\n");
    pi = 0.0;
    items_num = items;
    threads_num = threads;

    pthread_t thread[threads_num];
    int ids[threads_num];
    int i;

    for (i = 0; i < threads_num; i++)
    {
        ids[i] = i;
        pthread_create(&thread[i], NULL, compute_pi, &ids[i]);
    }

    for (i = 0; i < threads_num; i++)
    {
        pthread_join(thread[i], NULL);
    }

    return pi;
}
