# =========== Load converted depth.csv files =========== #

df1 <- read.csv("/Users/guillermocomesanacimadevila/Desktop/depth_1.csv", header=TRUE)
df2 <- read.csv("/Users/guillermocomesanacimadevila/Desktop/depth_2.csv", header=TRUE)
df3 <- read.csv("/Users/guillermocomesanacimadevila/Desktop/depth_3.csv", header=TRUE)

depth1 <- df1$depth
depth2 <- df2$depth
depth3 <- df3$depth

mean_depth1 <- mean(depth1, na.rm=TRUE)
mean_depth2 <- mean(depth2, na.rm=TRUE)
mean_depth3 <- mean(depth3, na.rm=TRUE)

print(paste("The average depth for depth_1.csv is:", mean_depth1))
print(paste("The average depth for depth_2.csv is:", mean_depth2))
print(paste("The average depth for depth_3.csv is:", mean_depth3))


# =========== Identified indel positions in sample 1  =========== #

Indel_position <- c(1245282, 1250728, 1245688, 1246270, 1246303, 1246787, 1246855, 
                    1251945, 1246874, 1247160, 1253892, 1254961, 1247083, 1247664, 
                    1247858, 1255000, 1248019, 1248343, 1252866, 1248727, 1248735, 
                    1254840, 1248813, 1248904, 1252271, 1249095, 1249404, 1249599, 
                    1250146, 1250200, 1250529, 1250927, 1251358, 1254381, 1251466, 
                    1251694, 1253106, 1253502, 1253854, 1254033, 1254066, 1254357)

# =========== Loop through all 3 tables and print depth at each position across 3 samples (gene duplication?)  =========== #

for (position in Indel_position) {
  index1 <- which(df1$position == position)
  index2 <- which(df2$position == position)
  index3 <- which(df3$position == position)
  
  depth_val1 <- ifelse(length(index1) > 0, df1$depth[index1], NA)
  depth_val2 <- ifelse(length(index2) > 0, df2$depth[index2], NA)
  depth_val3 <- ifelse(length(index3) > 0, df3$depth[index3], NA)
  
  cat(paste("Position:", position, "\n"))
  cat(paste("  Depth in depth_1.csv:", depth_val1, "\n"))
  cat(paste("  Depth in depth_2.csv:", depth_val2, "\n"))
  cat(paste("  Depth in depth_3.csv:", depth_val3, "\n\n"))
}