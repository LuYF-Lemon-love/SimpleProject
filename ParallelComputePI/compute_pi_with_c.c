#include <stdio.h>
#include <pthread.h>
#include <sys/time.h>

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

int main(){

    //printf("并行计算 PI 值，输入项数和线程数：\n");
    //scanf("%lld", &items_num);
    //scanf("%d", &threads_num);
    //printf("请耐心等待...\n");
    //items_num = 1e10;
    //threads_num = 4;

    int threads_array[] = {1, 2, 4, 8, 16};
    long long items_array[] = {1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10};
    int index_threads_array, index_items_array, epoch;
    int len_threads_array = sizeof(threads_array)/sizeof(int);
    int len_items_array = sizeof(items_array)/sizeof(long long); 
    long double sum_time, avg_time;
    
    for(index_threads_array = 0; index_threads_array < len_threads_array; index_threads_array++)
    {
        threads_num = threads_array[index_threads_array];

        for(index_items_array = 0; index_items_array < len_items_array; index_items_array++)
        {
            items_num = items_array[index_items_array];
            sum_time = 0.0;

            for(epoch = 0; epoch < 5; epoch++)
            {
                pi = 0.0;

                struct timeval start, end;
                gettimeofday(&start, NULL);

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

                gettimeofday(&end, NULL);

                long double time_use = 1000000 * (end.tv_sec - start.tv_sec) + end.tv_usec - start.tv_usec;
                sum_time += time_use;

                //printf("第 %d 次：用 %lld 个项和 %d 个线程并行计算的 PI = %.20Lf, 用时 %.6Lf 秒.\n", epoch, items_num, threads_num, pi, time_use/1000000.0);
            }

            avg_time = sum_time / 5;
            printf("用 %lld 个项和 %d 个线程并行计算的 PI = %.20Lf, 平均用时 %.6Lf 秒.\n", items_num, threads_num, pi, avg_time/1000000.0);
        }
    } 

    return 0;
}
